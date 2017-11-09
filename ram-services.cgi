#!/bin/bash

source /u2/data/LIB-SQLITE
DATABASE="/u2/data/services.db"
TABLE="services"


######################################################### HTML SECTION #########################################################

## HTML HEADER ##
cat ram-header

## HTML BODY ##
cat ram-app_bar

## HTML CONTAIN ##
cat<<EndCat
        <div class="container page-content">
            <div class="no-margin-left no-margin-right header text-light">List Services</div>  
            <br>     

            <table class="dataTable border bordered " data-role="datatable" data-auto-width="false">
                <thead>
                <tr>                  
                    <td class="sortable-column">NAME</td>
                    <td class="sortable-column">SERVICE</td>
                    <td class="sortable-column">DESCRIPTION</td>
                    <td class="sortable-column">LINK</td>
                    <td class="sortable-column">STATUS</td>
                </tr>
                </thead>
                
                <tbody>
EndCat

IFS='|'
SELECT-QUERY | while read NAME SERVICE DESCRIPTION LINK
do
    STATUS=""
    STAT=$(systemctl status $NAME | grep Active:)
    if [[ $STAT == *running* ]]
    then
        STATUS="Running"
    elif [[ $STAT == *dead* ]]
    then
        STATUS="Stopped"
    fi

cat<<EndCat
                    <tr>
                        <td>$NAME</td>
                        <td>$SERVICE</td>
                        <td>$DESCRIPTION</td>
                        <td><a href="http://$LINK" target="_blank">$LINK</td>                    
                        <td>$STATUS</td>
                    </tr>
EndCat
done

cat<<EndCat
                </tbody>
            </table>

EndCat

## HTML FOOTER ##
cat ram-footer
