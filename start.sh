#!/bin/bash
 
Dir="${1:-"/OVPs"}"

if [ -d "/data/" ]; then
    echo "持久化启动"
    if [ ! -f "/data/db.sqlite3" ]; then
        echo "第一次启动"
        mv db.sqlite3 /data/db.sqlite3
        ln -s /data/db.sqlite3 ${Dir}
    else
        echo "启动链接"
        rm db.sqlite3
        ln -s /data/db.sqlite3 ${Dir}
    fi
else
    echo "无持久化启动"
fi
cd ${Dir}

make run
