# Password Manager CLI tool

Major changes are on the way. Getting rid of old, using method. 
New updates will be based on command-line usage.

You can add passwords for following platform:
1. Instagram
2. Facebook
3. Gmail
4. Outlook
5. Twitter

```
./password_manager.py --platform instagram --add-password

 Username: ( User input required )
 Password: ( User input required )
-------------------------------------------------------

./password_manager.py --platform instagram --username dhruvik --get-password / --delete-password
Password: ( User inpur required )
-------------------------------------------------------

./password_manager --factory-reset
Master Password: ( User input required )
  
  >> This will remove all the files related to this tool.
```

Note: 
To check the password, no input is required from user. But, you will be asked to verify yourself at the time of delete operation. I am trying to make this tool as dynamic as possible, so you can add more platform which are not available by default.

Check out branch [main-outdated](https://github.com/dhruvikmevada/password_manager/tree/main-outdated) for boring usage.
