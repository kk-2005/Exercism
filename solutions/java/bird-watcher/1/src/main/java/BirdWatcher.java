class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public static int[] getLastWeek() {
        return new int[] {0, 2, 5, 3, 7, 8, 4};
    }

    public int getToday() {
        if (this.birdsPerDay.length == 0) {
            return 0;
        }
        return this.birdsPerDay[this.birdsPerDay.length - 1];
    }

    public void incrementTodaysCount() {
        if (this.birdsPerDay.length > 0) {
            this.birdsPerDay[this.birdsPerDay.length - 1]++;
        }
    }

    public boolean hasDayWithoutBirds() {
        // FIX 1: Switched from getLastWeek() to this.birdsPerDay
        for (int i = 0; i < this.birdsPerDay.length; i++) {
            if (this.birdsPerDay[i] == 0) {
                return true;
            }
        }
        return false;
    }

    public int getCountForFirstDays(int numberOfDays) {
        int count = 0;
        // FIX 2: Switched to this.birdsPerDay and capped the loop limit safely
        int limit = Math.min(numberOfDays, this.birdsPerDay.length);
        
        for (int i = 0; i < limit; i++) {
            count += this.birdsPerDay[i];
        }
        return count;
    }

    public int getBusyDays() {
        int count = 0;
        // FIX 3: Switched from getLastWeek() to this.birdsPerDay
        for (int i = 0; i < this.birdsPerDay.length; i++) {
            if (this.birdsPerDay[i] >= 5) {
                count++;
            }
        }
        return count;
    }
}

