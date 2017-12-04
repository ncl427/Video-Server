# Video-Server
<h2>Introduction</h2>
This document is to provide a <b>way of creating a video-streaming site</b> using an advanced python-based framework termed as django. As any of the system can be implemented in many ways we want to. But this document provides a way to use my code provided on the following link. 

<h2>Prerequisites & Pre-checks</h2>
Before using this server, you have to fulfil these requirements to make sure that the video-server works
<ol>
<li>&nbsp;should have the package <code>python-3</code> installed on the system</li>
<li>&nbsp;should have <code>django</code> installed on the system</li>
<li>&nbsp;should have <code>windows/ubuntu</code> as an operating system</li>
<li>&nbsp;should have system <code>environment-variables</code> defined for python-package</li>
</ol>

<h2>Steps to setup video server</h2>
The following steps are required to setup the server

<ol>
<li>&nbsp;Copy the code provided on GitHub</li>
<li>&nbsp;Move the code to some directory where you want to deploy</li>
<li>&nbsp;If you want to run the server on <code>localhost</code> i.e. 127.0.0.1 (on the same machine), your server has been deployed</li>

<li>&nbsp;Else if you want the server to run and to be accessed from a different machine, you have to modify the settings file
<ul>
<li>go to command-line and get the ip, using <code>ifconfig</code></li>
<li>go to setting.py file of the directory: <code>~/website/settings.py</code></li>
<li>search for the line, in which <code>ALLOWED_HOSTS</code> is mentioned</li>
<li>replace the code-line with this</li>
<li><code>['<b>systems_ip</b>', 'localhost', '127.0.0.1']</code></li>
</ul>
</li>

</ol>

<h2>Commands to run the server</h2>
The following steps are required to setup the server
<ol>
<li>&nbsp;Go to <code>root</code> directory of the project</li>
<li>&nbsp;Run this command:
<ul><li><code>python manage.py runserver</code></li></ul>
</li>
</ol>

At the end you should be able to see the screen below. If yes, your server is ready to be accessed from any of the browser to which your ip is accessible through any interface you’ve defined.

![Alt text](http://www.google.com/logos/doodles/2015/googles-new-logo-5078286822539264.3-hp2x.gif "Optional Title")

<h2>*Note:</h2>
If you’re accessing the website address from linux machine, then you need to install <code>chromium</code> in that case, because the <code>static</code> media used in the project is not accessible in Mozilla only in case if you’re using linux. So <code>Chrome/Chromium</code> browser is recommended.
