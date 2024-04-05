#!/bin/bash

cargo run --manifest-path rust/Cargo.toml


# --[INCASE RUST CRASHES]--

# pid of python
pid=$(ps aux | grep python | grep -v grep | awk '{print $2}')
kill -s KILL $pid # kill the pid