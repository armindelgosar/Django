import java.util.ArrayList;

public class Advertiser extends BaseAdvertising {
    private static ArrayList<Advertiser> advertisers = new ArrayList<>();
    private int id;
    private String name;
    private int clicks = 0;
    private int views = 0;

    public Advertiser(int id, String name) {
        this.id = id;
        this.name = name;
        advertisers.add(this);
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }


    public static void help() {
        System.out.println("This class saves each Advertiser's id, name, clicks and views!");
    }

    @Override
    public void describeMe() {
        System.out.println("This class's responsibility is maintaining system's advertiser's data!");
    }

    public static void getTotalClicks() {
        for (Advertiser advertiser : advertisers) {
            System.out.println(advertiser.getName() + ": " + advertiser.clicks);
        }
    }


}
