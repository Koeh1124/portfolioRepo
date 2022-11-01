public class Category{
    private String name;
    private Account[] accounts;

    //initilizers
    Category(String name){
        this.name = name; 
        this.accounts = new Account[0];   
    }

    Category(String name, Account[] accounts){
        this.name = name; 
        this.accounts = accounts;
    }

    //getters
    public String getName(){
        return this.name;
    }

    public Account[] getAccounts(){
        return this.accounts;
    }

    //setters
    public void setName(String name){
        this.name = name;
    }

    //methods
    public void addAccount(Account acc){
        Account[] newAccounts = new Account[this.accounts.length+1];
        for (int i = 0;i<this.accounts.length;i++){
            newAccounts[i] = this.accounts[i];
        }
        newAccounts[this.accounts.length] = acc;
        this.accounts = newAccounts;
    }

    public void removeAccount(int index){
        Account[] newAccounts = new Account[this.accounts.length-1];
        for (int i = 0;i<index;i++){
            newAccounts[i] = this.accounts[i];
        }
        for (int i = index+1;i<newAccounts.length;i++){
            newAccounts[i] = this.accounts[i+1];
        }
        this.accounts = newAccounts;
    }

    public void removeAccount(Account acc){
        for(int i = 0;i<this.accounts.length;i++){
            if(acc.equals(this.accounts[i])){
                removeAccount(i);
                return;
            }
        }
    }

    public boolean equals(Category category){
        if(!this.name.equals(category.name)||!(this.accounts.length==category.accounts.length)){
            return false;
        }
        for(int i = 0;i<this.accounts.length;i++){
            if(!(this.accounts[i].equals(category.accounts[i]))){
                return false;
            }
        }
        return true;
    }
}