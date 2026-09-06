public class SqueakyClean {
    public static String clean(String identifier) {
        StringBuilder result = new StringBuilder();
        boolean capitalizeNext = false;
        for (char ch : identifier.toCharArray()) {
            // Replace spaces with underscores
            if (ch == ' ') {
                result.append('_');
            }
            // Convert kebab-case to camelCase
            else if (ch == '-') {
                capitalizeNext = true;
            }
            // Convert leetspeak
            else if (ch == '4') {
                result.append('a');
            }
            else if (ch == '3') {
                result.append('e');
            }
            else if (ch == '0') {
                result.append('o');
            }
            else if (ch == '1') {
                result.append('l');
            }
            else if (ch == '7') {
                result.append('t');
            }
            // Keep letters and handle capitalization
            else if (Character.isLetter(ch)) {
                if (capitalizeNext) {
                    result.append(Character.toUpperCase(ch));
                    capitalizeNext = false;
                } else {
                    result.append(ch);
                }
            }
        }

        return result.toString();
    }
}