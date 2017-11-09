#!/bin/bash

# LOGIC #
eval "`/u2/files/proccgi $*`"

if [ "$FORM_SUBMIT" = "SuBM1t" ]
then
    case $SERVICE_PORT in
      FTP)  echo "-A INPUT -p tcp	-s $ENTRY_VALUE -m state --state NEW -m tcp --dport 21  -j ACCEPT" >> /u/02.1.SCRIPT-RAW/IPTABLES-GEN/01.FTP;;
      SSH)  echo "-A INPUT -p tcp	-s $ENTRY_VALUE -m state --state NEW -m tcp --dport 22  -j ACCEPT" >> /u/02.1.SCRIPT-RAW/IPTABLES-GEN/02.SSH;;
      TELNET) echo "-A INPUT -p tcp	-s $ENTRY_VALUE -m state --state NEW -m tcp --dport 23  -j ACCEPT" >> /u/02.1.SCRIPT-RAW/IPTABLES-GEN/03.TELNET;;
      OTHERS_IP) echo "-A INPUT -p tcp	-s $ENTRY_VALUE -m state --state NEW -m tcp -j ACCEPT" >> /u/02.1.SCRIPT-RAW/IPTABLES-GEN/50.OTHERS;;
      OTHERS_PORT) echo "-A INPUT -p tcp -m state --state NEW -m tcp --dport $ENTRY_VALUE -j ACCEPT" >> /u/02.1.SCRIPT-RAW/IPTABLES-GEN/50.OTHERS;;
      BLOCK_IP) echo "-A INPUT -p tcp	-s $ENTRY_VALUE -m state --state NEW -m tcp -j REJECT" >> /u/02.1.SCRIPT-RAW/IPTABLES-GEN/98.BLOCK;;
    esac
    sudo /u2/IPTABLES-GEN/iptables_gen.sh
fi

## HTML HEADER ##
cat ram-header

## HTML BODY ##
cat ram-app_bar

## HTML CONTAIN ##
cat<<EndCat
        <div class="container page-content">
            <div class="login-form padding20 block-shadow">
                <form METHOD=POST>
                    <h1 class="text-light">Tambah IP Akses</h1>
                    <hr class="thin"/>
                    <h4> IP Dirimu : $REMOTE_ADDR | </h4>
                    <br />
                    <h4> Entry Input Value</h4>
                    <div class="input-control modern text full-size" data-role="input">
                    <input type="text" name="ENTRY_VALUE">
                        <span class="label">Nilai Masukan</span>
                        <span class="informer">Silahkan masukan Nilai Masukan</span>
                        <span class="placeholder">Nilai Masukan</span>
                        <button class="button helper-button clear"><span class="mif-cross"></span></button>
                    </div>
                    <br />
                    <br />
                    <h4> Entry Service Port</h4>
                    <div class="input-control modern select full-size">
                        <select name="SERVICE_PORT">
                          <option value="SSH">SSH</option>
                          <option value="FTP">FTP</option>
                          <option value="TELNET">Telnet</option>
                          <option value="OTHERS_IP">Others by IP</option>
                          <option value="OTHERS_PORT">Others by Port</option>
                          <option value="BLOCK_IP">Block IP Address</option>
                        </select>
                    </div>
                    <br />
                    <br />
                    <br />
                    <div class="form-actions">
                        <button type="submit" class="button primary" VALUE="SuBM1t" NAME="FORM_SUBMIT">Save</button>
                    </div>
                </form>
            </div>
        </div>
EndCat

## HTML FOOTER ##
cat ram-footer
