public class LogLevels {
    
    public static String message(String logLine) {
        String[] msg = logLine.split(":");
        String s1=msg[1];
        s1=s1.trim();
        return s1;
    }

    public static String logLevel(String logLine) {
        String[] msg = logLine.split(":");
        String s1=msg[0];
        String s2=s1.substring(1, s1.length() - 1);
        String s3=s2.toLowerCase();
        return s3;
    }

    public static String reformat(String logLine) {
        String s1=message(logLine);
        String s2=logLevel(logLine);
        String s3=s1+" ("+s2+")";
        return s3;
    }
}
