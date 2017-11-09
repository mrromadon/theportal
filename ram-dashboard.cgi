#!/bin/bash

echo "REMOTE_ADDR=$REMOTE_ADDR" > ram-data

## HTML HEADER ##
cat ram-header

## HTML BODY ##
cat ram-app_bar

## HTML CONTAIN ##
cat<<EndCat
        <div class="container page-content align-center">
            <br />
            <h1 style="font-size: 4.5rem; line-height: 1" class="text-shadow metro-title text-light">DASHBOARD</span></h1>
            <div class="no-margin-left no-margin-right header text-light">
                Dashboard Page <a href="https://www.mrromadon.tk/app/ram-dashboard.cgi">mrromadon.tk</a> Apps
            </div>
        </div>
EndCat

## HTML FOOTER ##
cat ram-footer
