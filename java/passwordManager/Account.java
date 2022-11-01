/*
 * Reqs:
 * name - String
 * userName - String
 * password - Password
 * category - class?
 */
public class Account {
    // init vars for class
    private String name;
    private String user;
    private Password password;

    // init statements (one w/password input and one w/o)
    public Account(String name, String user, Password password) {
        this.name = name;
        this.user = user;
        this.password = password;
    }

    public Account(String name, String user, String password) {
        this.name = name;
        this.user = user;
        this.password = new Password(password);
    }

    public Account(String name, String user) {
        this.name = name;
        this.user = user;
        this.password = new Password();
    }

    // getters
    public String getName() {
        return this.name;
    }

    public String getUser() {
        return this.user;
    }

    public Password getPassword() {
        return this.password;
    }

    // setters
    public void setName(String name) {
        this.name = name;
    }

    public void setUser(String user) {
        this.user = user;
    }

    // Pass in either a Password object or a String to set to new password
    public void setPassword(String password) {
        this.password = new Password(password);
    }

    public void setPassword(Password password) {
        this.password = password;
    }

    // geterate completely new password
    public void newPassword() {
        this.password = new Password();
    }

    // toString
    @Override
    public String toString() {
        return String.format("%s:\n\tUser Name:\t%s\n\tPassword:\t%s", this.name, this.user, this.password);
    }
    /*
     * Returns information inf following format
     * "
     * {Account Name}:
     * User Name: {userName}
     * Password: {Passwprd}
     * "
     */

     public boolean equals(Account acc){
        return (this.name.equals(acc.name))&&(this.password.equals(acc.password))&&(this.user.equals(acc.user));
     }
}
