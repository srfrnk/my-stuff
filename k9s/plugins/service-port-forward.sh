#!/bin/bash
kubectl port-forward --context $1 -n $2 svc/$3 $(kubectl get -o jsonpath='{.metadata.annotations.k9scli\.io/auto-portforwards}' --context $1 -n $2 svc/$3)
sleep 10
