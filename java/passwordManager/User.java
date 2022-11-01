public class User {
    private String userName;
    private Category[] categories;

    User(String userName){
        this.userName = userName;
        this.categories = new Category[0];
    }

    User(String userName, Category[] categories){
        this.userName = userName;
        this.categories = categories;
    }

   //getters
   public String getUSerName(){
    return this.userName;
    }

    public Category[] getCategories(){
        return this.categories;
    }

    //setters
    public void setUserName(String userName){
        this.userName = userName;
    }
    
    //methods
    public void addCategory(Category category){
        Category[] newCategories = new Category[this.categories.length+1];
        for(int i = 0;i<this.categories.length;i++){
            newCategories[i] = this.categories[i];
        }
        newCategories[this.categories.length] = category;
        this.categories = newCategories;
    }

    public void removeCategory(int index){
        Category[] newCategories = new Category[this.categories.length-1];
        for (int i = 0;i<index;i++){
            newCategories[i] = this.categories[i];
        }
        for (int i = index+1;i<newCategories.length;i++){
            newCategories[i] = this.categories[i+1];
        }
        this.categories = newCategories;
    }

    public void removeCategory(Category cat){
        for(int i = 0;i<this.categories.length;i++){
            if(cat.equals(this.categories[i])){
                removeCategory(i);
                return;
            }
        }
    }
}
