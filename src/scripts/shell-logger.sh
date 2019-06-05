#!/usr/bin/env bash
function log() {

    MSG="[`date "+%Y-%m-%d %H:%M:%S"`] [$1] $2"
    echo ${MSG}
    echo ${MSG} >> "run-me.log"
}