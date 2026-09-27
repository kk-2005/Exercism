public class JedliksToyCar {
    public int distance = 0;
    public int battery = 100;

    public static JedliksToyCar buy() {
        JedliksToyCar car = new JedliksToyCar();
        return car;
    }

    public String distanceDisplay() {
        // Fixed spelling from "metres" to "meters"
        return "Driven " + this.distance + " meters"; 
    }

    public String batteryDisplay() {
        // Added the requirement for when the battery is empty
        if (this.battery == 0) {
            return "Battery empty";
        }
        return "Battery at " + this.battery + "%";
    }

    public void drive() {
        if (this.battery > 0) {
            this.distance = this.distance + 20;
            this.battery = this.battery - 1;
        }
        // Removed System.out.print to avoid unexpected test failures
    }
}
