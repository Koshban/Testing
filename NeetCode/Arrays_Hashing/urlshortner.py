'''
Set up a new Flask project.
Define the necessary routes for the API endpoints.
Implement the logic for generating short URLs.
Create a database to store the original and short URLs.
Implement API endpoints for creating and accessing short URLs.

Requirements

Functional Requirements
--------------------
URL shortening Service similar to TinyURL, or Bitly
A client (user) enters a long URL into the system and the system returns a shortened URL
The client visiting the short URL must be redirected to the original long URL
Multiple users entering the same long URL must receive the same short URL (1-to-1 mapping)
The short URL should be readable
The short URL should be collision-free
The short URL should be non-predictable
The client should be able to choose a custom short URL
The short URL should be web-crawler friendly (SEO)
The short URL should support analytics (not real-time) such as the number of redirections from the shortened URL
The client optionally defines the expiry time of the short URL

Non-Functional Requirements
-------------------
High Availability
Low Latency
High Scalability
Durable
Fault Tolerant

HTTP request:
--------------
/url
method: PUT
accept: application/JSON
accept-encoding: gzip, deflate, br
accept-language: en-us
authorization: Bearer <JWT>
content-length: 150
content-type: application/JSON
content-encoding: gzip
cookie: id=xyz;
user-agent: Chrome

{
    long-url: "https://en.wikipedia.org/wiki/URL_shortening",
    tags: ["productivity"],
    expires: "datetime",
    custom: "short-id" (optional)

}

HTTP Response :
---------------
status code: 200 OK
cache-control: no-cache, private
content-encoding: gzip
content-language: en-us
content-type: application/JSON
date: server-datetime
set-cookie: x=abc; expires=datetime;
           SameSite=strict; HttpOnly; secure

{
    long-url: "https://en.wikipedia.org/wiki/URL_shortening",
    short-url: "xy725ab",
    created-at: datetime,
    is-active: True
}
'''
from flask import Flask, request, redirect
import string
import random
import sqlite3

app = Flask(__name__)

# Create a random string for short URLs
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# Create a database connection and table
conn = sqlite3.connect('urls.db')
conn.execute('CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY AUTOINCREMENT, original_url TEXT NOT NULL, short_url TEXT NOT NULL, expiry_time DATETIME)')

# API endpoint for creating short URLs
@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    custom_short_url = request.form.get('custom_short_url')
    expiry_time = request.form.get('expiry_time')
    
    # Check if the custom short URL already exists
    if custom_short_url:
        cursor = conn.execute('SELECT * FROM urls WHERE short_url = ?', (custom_short_url,))
        result = cursor.fetchone()
        if result:
            return 'Custom short URL already exists. Please choose a different one.'
    
    # Generate a unique short URL
    short_url = generate_short_url()
    if custom_short_url:
        short_url = custom_short_url
    
    # Store the original URL, short URL, and expiry time in the database
    conn.execute('INSERT INTO urls (original_url, short_url, expiry_time) VALUES (?, ?, ?)', (original_url, short_url, expiry_time))
    conn.commit()
    
    return short_url

# API endpoint for accessing the original URL
@app.route('/<short_url>')
def redirect_url(short_url):
    # Retrieve the original URL from the database
    cursor = conn.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    
    if result:
        original_url = result[0]
        
        # Update analytics for the short URL (e.g., count redirections)
        conn.execute('UPDATE urls SET redirections = redirections + 1 WHERE short_url = ?', (short_url,))
        conn.commit()
        
        return redirect(original_url)
    else:
        return 'Invalid URL'

if __name__ == '__main__':
    app.run(debug=True)