# JailMaster 🚀

Welcome to JailMaster, your go-to Python application for managing and monitoring user login credentials. Because even jails need good management! 🏢🔒 This README provides the scoop on setting up, running, and contributing to the project. Buckle up, we're on a mission! 🤠

🔗 [JailMaster Repository](https://github.com/j-a-y-e-s-h/jailmaster.git)

## Video Demo

- [Link to Video Demo]

## Installation 🛠️

1. Clone the repository:

   ```bash
   git clone https://github.com/j-a-y-e-s-h/jailmaster.git
   ```
2. Install the required dependencies:

   - tkinter
   - mysql-connector-python
   - numpy
   - matplotlib==3.2.0
   - python_dotenv

   ```bash
   pip install tkinter mysql-connector-python numpy matplotlib==3.2.0 python_dotenv
   ```

   or
    ```bash
   pip install -r requirements.txt
   ```
4. Navigate to the `JAILMASTER` folder. If you get lost, don't worry – it's just a virtual jailbreak! 🏃‍♂️

### Setup the Database 💾

To create the database using the MySQL schema:

1. Copy-paste the contents of `querys.sql` directly into the MySQL command line, or
2. Use the command (from cmd):

   ```shell
   mysql -u <mysql-username> -p<mysql-password> < querys.sql
   ```

   - Replace `<mysql-username>` and `<mysql-password>` with your credentials.

   ( **Note**: Don't include the "<>" angular brackets in the command. Security, you know!)
3. Create a `.env` file if not exist and add(change your password and username): 

   ```sql
   DB_PASSWORD="your_password"
   DB_USER="your_username"
   ```
4. Run the application with the passion of an escaped convict:

   ```bash
   python main.py
   ```

### Installing Fonts 🖋️

For optimal GUI appearance, install the Montserrat font. From the `assets` folder, double click on each font file with `.ttf` format. Make it look snazzy!

If issues persist, research or create a new issue for assistance. We're not abandoning you in digital jail. 🆘

## Extras 🎉

Explore additional features of the app:

### Adding New Users 🤓

To add new login credentials:

```sql
INSERT INTO login (username, password) VALUES ("your-username", "your-password");
```

( **PS**: Direct database interactions are required for this feature. It's like breaking into the secret vault – but legal!)

[⬆️ Back to Top](https://github.com/j-a-y-e-s-h/jailmaster/blob/main/readme.md#jailmaster-)

# Contributing 🤝

Contributors to JailMaster:

* [Jayesh](https://github.com/j-a-y-e-s-h)
* [Yash](https://github.com/YashPatil2023/)
* [Kamlesh](https://github.com/kamlesh-IY9/)

<p align="center"> 
  <a href="https://python.org"><img src="http://forthebadge.com/images/badges/made-with-python.svg" alt="made-with-python"></a> 
  <br> 
  <img src="https://img.shields.io/github/contributors/j-a-y-e-s-h/jailmaster?style=for-the-badge" alt="Contributors"> 
![Repository Size](https://img.shields.io/github/repo-size/j-a-y-e-s-h/jailmaster?style=for-the-badge)
 <br> 
  <img src="https://img.shields.io/github/watchers/j-a-y-e-s-h/jailmaster?style=for-the-badge" alt="Watchers"> 
  <img src="https://img.shields.io/github/commit-activity/w/j-a-y-e-s-h/jailmaster?style=for-the-badge" alt="Commit Activity"> 
  <img src="https://img.shields.io/github/issues/j-a-y-e-s-h/jailmaster?style=for-the-badge" alt="Issues"> 
</p>

**Made with ❤️ and Python!**

Keep coding, and let bugs be the only creatures to fear in your code! 🐞✨
