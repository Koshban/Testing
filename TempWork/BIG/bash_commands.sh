# Bash one-liner to find and kill zombie processes across a cluster, then explain PID 1's role in cleanup.
ps aux| awk '$8=="Z" {print $2}'|xargs -r kill -HUP
# wrap the above to run across cluster
for i in $(cat /nodeslist.txt); do ssh -o StrictHostKeyChecking=no $i "ps aux| awk '\$8==\"Z\" {print \$2}'|xargs -r kill -HUP";done

# How do you handle signals (SIGTERM, SIGKILL) in Bash/Python scripts for graceful shutdowns during deployments?
cleanup(){
    echo "Cleaning Up..."
    kill $(jobs -p) 2 >/dev/null
}

trap cleanup SIGTERM SIGINT
trap - SIGKILL