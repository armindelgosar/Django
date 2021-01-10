public class BaseAdvertising {
    private int clicks;
    private int views;

    public int getClicks() {
        return this.clicks;
    }

    public int getViews() {
        return this.views;
    }
    public void incClicks(){
        this.clicks += 1;
    }
    public void incViews(){
        this.views += 1;
    }
    public void describeMe(){
        System.out.println("Nothing!");
    }
}
