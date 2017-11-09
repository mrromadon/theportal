#!/bin/bash

# LOGIC #
eval "`/u2/files/proccgi $*`"
source /u2/data/LIB-SQLITE

if [ "$FORM_SURE" = "SuRe" ]
then
    INSERT-QUERY /u2/data/services.db services
fi

## HTML HEADER ##
cat ram-header

## HTML BODY ##
cat ram-app_bar

## HTML CONTAIN ##
cat<<EndCat
        <div class="container page-content">
            <div class="login-form padding20 block-shadow">
                <form>
                    <h1 class="text-light">Add New Services</h1>
                    <hr class="thin"/>
                    <br />
                    <div class="input-control modern text full-size" data-role="input">
                        <input type="text" name="SERVICE_NAME">
                        <span class="label">Nama Service:</span>
                        <span class="informer">Please enter the service name</span>
                        <span class="placeholder">Service Name</span>
                        <button class="button helper-button clear"><span class="mif-cross"></span></button>
                    </div>
                    <br />
                    <div class="input-control modern text full-size" data-role="input">
                        <input type="text" name="SERVICE_SERVICE">
                        <span class="label">Jenis Service:</span>
                        <span class="informer">Please enter the service spesific</span>
                        <span class="placeholder">Jenis Service</span>
                        <button class="button helper-button clear"><span class="mif-cross"></span></button>
                    </div>
                    <br />
                    <div class="input-control modern text full-size" data-role="input">
                        <input type="text" name="SERVICE_DESCRIPTION">
                        <span class="label">Description:</span>
                        <span class="informer">Please enter the service description</span>
                        <span class="placeholder">Service Description</span>
                        <button class="button helper-button clear"><span class="mif-cross"></span></button>
                    </div>
                    <br />
                    <div class="input-control modern text full-size" data-role="input">
                        <input type="text" name="SERVICE_LINK">
                        <span class="label">Link Service:</span>
                        <span class="informer">Please enter the service link</span>
                        <span class="placeholder">Service Link</span>
                        <button class="button helper-button clear"><span class="mif-cross"></span></button>
                    </div>
                    <br />
                    <div class="form-actions">
                        <button type="submit" class="button primary" VALUE="SuBM1t" NAME="FORM_SUBMIT">Save</button>
                        <button type="button" class="button link">Cancel</button>
                        <INPUT TYPE="CHECKBOX" NAME="FORM_SURE"   VALUE="SuRe"> I am sure !<BR>
                    </div>
                </form>
            </div>
        </div>
EndCat

## HTML FOOTER ##
cat ram-footer
