#!/bin/bash

TOPIC="lampu/kamar"

# LOGIC #
eval "`/u/04.www/html/files/proccgi $*`"

if [ "$FORM_SUBMIT" = "blue_aktif" ]
then
    mosquitto_pub -h localhost -t $TOPIC -m "BLUE-ON $(date +"%Y/%m/%d %H:%M:%S")"
fi
if [ "$FORM_SUBMIT" = "blue_mati" ]
then
    mosquitto_pub -h localhost -t $TOPIC -m "BLUE-OFF $(date  +"%Y/%m/%d %H:%M:%S")"
fi
if [ "$FORM_SUBMIT" = "red_aktif" ]
then
    mosquitto_pub -h localhost -t $TOPIC -m "RED-ON $(date +"%Y/%m/%d %H:%M:%S")"
fi
if [ "$FORM_SUBMIT" = "red_mati" ]
then
    mosquitto_pub -h localhost -t $TOPIC -m "RED-OFF $(date  +"%Y/%m/%d %H:%M:%S")"
fi
if [ "$FORM_SUBMIT" = "green_aktif" ]
then
    mosquitto_pub -h localhost -t $TOPIC -m "GREEN-ON $(date +"%Y/%m/%d %H:%M:%S")"
fi
if [ "$FORM_SUBMIT" = "green_mati" ]
then
    mosquitto_pub -h localhost -t $TOPIC -m "GREEN-OFF $(date  +"%Y/%m/%d %H:%M:%S")"
fi

## HTML HEADER ##
cat ram-header

## HTML BODY ##
cat ram-app_bar

## HTML CONTAIN ##
cat<<EndCat
        <div class="container page-content">
            <div class="login-form padding20 block-shadow">
                <form action="ram-dashboard.cgi" method=POST>
                    <h1 class="text-light">SMART HOME</h1>
                    <hr class="thin"/>
                    <br />
                    <div class="form-actions">
                        <button type="submit" class="button primary bg-blue large-button" VALUE="blue_aktif" NAME="FORM_SUBMIT">ON</button>
                        <button type="submit" class="button primary bg-blue large-button" VALUE="blue_mati" NAME="FORM_SUBMIT">OFF</button>
                        <br />
                        <br />
                        <br />
                        <button type="submit" class="button primary bg-red large-button" VALUE="red_aktif" NAME="FORM_SUBMIT">ON</button>
                        <button type="submit" class="button primary bg-red large-button" VALUE="red_mati" NAME="FORM_SUBMIT">OFF</button>
                        <br />
                        <br />
                        <br />
                        <button type="submit" class="button primary bg-green large-button" VALUE="green_aktif" NAME="FORM_SUBMIT">ON</button>
                        <button type="submit" class="button primary bg-green large-button" VALUE="green_mati" NAME="FORM_SUBMIT">OFF</button>
                    </div>
                </form>
            </div>
        </div>
EndCat

## HTML FOOTER ##
cat ram-footer
