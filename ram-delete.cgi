#!/bin/bash

# LOGIC #
eval "`/u2/files/proccgi $*`"
source /u2/data/LIB-SQLITE

if [ "$FORM_SURE" = "SuRe" ]
then
    DELETE-QUERY /u2/data/services.db SERVICES
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
                    <h1 class="text-light">Delete Existing Services</h1>
                    <hr class="thin"/>
                    <br />
                    <h5>Field Paramater</h5>
                    <div class="input-control modern select full-size">
                        <select name="FORM_FIELD">
                            <option value="NAME">Name</option>
                            <option value="SERVICE">Service</option>
                            <option value="DESCRIPTION">Description</option>
                            <option value="LINK">Link</option>
                        </select>
                    </div>
                    <br />
                    <div class="input-control modern text full-size" data-role="input">
                        <input type="text" name="FORM_VALUE">
                        <span class="label">Detail Value:</span>
                        <span class="informer">Please enter the spesific value</span>
                        <span class="placeholder">Input Value</span>
                        <button class="button helper-button clear"><span class="mif-cross"></span></button>
                    </div>
                    <br />
                    <div class="form-actions">
                        <button type="submit" class="button primary" VALUE="SuBM1t" NAME="FORM_SUBMIT">Delete</button>
                        <button type="button" class="button link">Cancel</button>
                        <INPUT TYPE="CHECKBOX" NAME="FORM_SURE"   VALUE="SuRe"> I am sure !<BR>
                    </div>
                </form>
            </div>
        </div>
EndCat

## HTML FOOTER ##
cat ram-footer
