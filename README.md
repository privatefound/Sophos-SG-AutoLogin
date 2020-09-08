<h1>Sophos SG Auto-Login&nbsp;&nbsp;<img src="https://www.sophos.com/en-us/medialibrary/SophosNext/Images/Navigation/Main/about-sophos-icon.svg?la=en"/></h1>

<p>This Script permit you to access to one or more Sophos SG Firewall automatically 
and give you the time to check the interfaces, atp and other alert on SG Dashboard</p>

<h4>Prerequisites</h4>
Python 3<br/>
Official google chrome version (not beta)<br/>
webbot library (<code>pip install webbot</code>)

<h4> Installation </h4>
Clone the Repository
<code>git clone https://github.com/privatefound/Sophos-SG-AutoLogin.git</code><br/>
Navigate inside the directory with <code>cd cd Sophos-SG-AutoLogin</code><br/>
Give login.py the permissions to be executed (if needed) with <code>sudo chmod +x login.py</code><br/>
Then modify the script and insert the Firewall ip that you need to log in and the password where indicated.<br/>
<code>login('<strong>insertiphere</strong>', '<strong>insertpasswordhere</strong>');</code><br/>
Now you can execute the script <code>./login.py</code>
