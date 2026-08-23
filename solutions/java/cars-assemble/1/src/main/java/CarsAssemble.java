public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        double success_rate=0.0;
        if (speed>=1 && speed<=4){
            success_rate=100.0;
        }
        else if (speed>=5 && speed<=8){
            success_rate=90.0;
        }
        else if (speed==9){
            success_rate=80.0;
        }
        else if (speed==10){
            success_rate=77.0;
        }
        double car_count=(success_rate*221*speed)/100;
        return car_count;
    }

    public int workingItemsPerMinute(int speed) {
        double car_per_hour=productionRatePerHour(speed);
        int car_per_min=(int)(car_per_hour/60.0);
        return car_per_min;
    }
}
