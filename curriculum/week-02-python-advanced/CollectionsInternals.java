import java.util.*;
import java.util.stream.*;

/*
 * Week 2 Saturday drill -- Java: collections internals, generics, Streams.
 * Predict-then-run, same protocol as Week 1's Gotchas.java.
 * Run: java CollectionsInternals.java   (JDK 11+, no javac step)
 */
public class CollectionsInternals {

    static Scanner sc = new Scanner(System.in);

    static void predict(int n, String title, String code, String question) {
        System.out.println("=".repeat(70));
        System.out.println("BLOCK " + n + ": " + title);
        System.out.println("=".repeat(70));
        System.out.println("CODE:");
        System.out.println(code);
        System.out.println("\nQUESTION: " + question);
        System.out.print(">>> Type your guess, then press Enter to reveal the real answer: ");
        sc.nextLine();
    }

    static void reveal(String answer, String why) {
        System.out.println("\nACTUAL ANSWER:");
        System.out.println("    " + answer);
        System.out.println("\nwhy: " + why + "\n\n");
    }

    public static void main(String[] args) {

        // -------------------------------------------------------------
        // BLOCK 1: generic type info is erased at runtime
        predict(1, "Generic type erasure -- what does the JVM actually know?",
            "List<String> strings = new ArrayList<>();\n" +
            "List<Integer> ints = new ArrayList<>();\n" +
            "System.out.println(strings.getClass() == ints.getClass());",
            "Does this print true or false -- are List<String> and List<Integer> the same class at runtime?");
        List<String> strings = new ArrayList<>();
        List<Integer> ints = new ArrayList<>();
        boolean sameClass = strings.getClass() == ints.getClass();
        reveal(String.valueOf(sameClass),
            "true -- generics exist only at COMPILE time, for the compiler to check your code. " +
            "At runtime both are just plain ArrayList objects; the <String> and <Integer> are erased. " +
            "This is exactly why `new T[]` doesn't compile and why `instanceof List<String>` is illegal -- " +
            "there is no type argument left at runtime to check against.");

        // -------------------------------------------------------------
        // BLOCK 2: Streams are lazy -- nothing runs without a terminal operation
        predict(2, "A Stream pipeline with no terminal operation",
            "List<Integer> nums = List.of(1, 2, 3);\n" +
            "Stream<Integer> s = nums.stream().peek(x -> System.out.println(\"peeked \" + x));\n" +
            "// ... and then nothing else is called on s",
            "Does \"peeked 1\", \"peeked 2\", \"peeked 3\" print, or does nothing print at all?");
        List<Integer> nums = List.of(1, 2, 3);
        Stream<Integer> s = nums.stream().peek(x -> System.out.println("    (would print: peeked " + x + ")"));
        reveal("nothing prints -- the peek() callback above never actually ran",
            "peek(), filter(), map() are all INTERMEDIATE operations -- they just build up a pipeline " +
            "description. Nothing executes until a TERMINAL operation (collect, forEach, count, findFirst...) " +
            "pulls elements through. A Stream with no terminal op does zero work, ever -- the line above " +
            "you just read printed nothing because it never actually ran.");

        // -------------------------------------------------------------
        // BLOCK 3: List.of() is genuinely immutable, not just conventionally
        predict(3, "List.of() and mutation",
            "List<String> fixed = List.of(\"a\", \"b\", \"c\");\n" +
            "fixed.add(\"d\");",
            "Does fixed.add(\"d\") work quietly, or throw? If it throws, what kind of exception?");
        List<String> fixed = List.of("a", "b", "c");
        String outcome;
        try {
            fixed.add("d");
            outcome = "added successfully -- no exception";
        } catch (UnsupportedOperationException e) {
            outcome = "UnsupportedOperationException: " + e;
        }
        reveal(outcome,
            "List.of() (Java 9+) returns a genuinely immutable list backed by a fixed-size internal array with " +
            "no add/remove/set support at all -- unlike Collections.unmodifiableList(), which just wraps a " +
            "mutable list and blocks writes through that ONE wrapper (the underlying list can still change if " +
            "something else holds a reference to it). List.of() has no mutable backing list to leak through.");

        // -------------------------------------------------------------
        // BLOCK 4: Collectors.groupingBy
        predict(4, "Collectors.groupingBy -- grouping without writing the loop yourself",
            "List<String> words = List.of(\"ant\", \"bee\", \"ape\", \"bat\", \"cat\");\n" +
            "Map<Character, List<String>> byFirst = words.stream()\n" +
            "    .collect(Collectors.groupingBy(w -> w.charAt(0)));",
            "What does byFirst look like -- what are the keys, and what's in each list?");
        List<String> words = List.of("ant", "bee", "ape", "bat", "cat");
        Map<Character, List<String>> byFirst = words.stream()
            .collect(Collectors.groupingBy(w -> w.charAt(0)));
        reveal(byFirst.toString(),
            "groupingBy(classifier) is the Streams equivalent of Python's defaultdict(list) pattern from " +
            "Week 1 -- one line replaces a manual HashMap<Character, List<String>> with computeIfAbsent calls. " +
            "Keys come from whatever the classifier function returns (here, charAt(0)); insertion order into " +
            "each list matches the stream's own order, but the KEY order in the map itself is not guaranteed " +
            "(HashMap, not LinkedHashMap) unless you pass groupingBy a map-supplier that says otherwise.");

        // -------------------------------------------------------------
        // BLOCK 5: findFirst short-circuits -- it doesn't process everything
        predict(5, "findFirst short-circuits a Stream pipeline",
            "List<Integer> data = List.of(1, 2, 3, 4, 5);\n" +
            "Optional<Integer> found = data.stream()\n" +
            "    .peek(x -> System.out.println(\"checking \" + x))\n" +
            "    .filter(x -> x > 2)\n" +
            "    .findFirst();",
            "Does \"checking\" print for all 5 elements, or does it stop early? If early, after which element?");
        List<Integer> data = List.of(1, 2, 3, 4, 5);
        Optional<Integer> found = data.stream()
            .peek(x -> System.out.println("    checking " + x))
            .filter(x -> x > 2)
            .findFirst();
        reveal("stops after checking element 3 -- found.get() = " + found.get(),
            "findFirst() is a SHORT-CIRCUITING terminal operation -- the moment filter() lets one element " +
            "through, the whole pipeline stops pulling more elements from the source. Elements 4 and 5 are " +
            "never even visited. This matters for cost: on a huge or infinite stream, findFirst/anyMatch/" +
            "limit can be the difference between O(1)-ish work and scanning everything.");

        System.out.println("=".repeat(70));
        System.out.println("SELF-CHECK");
        System.out.println("Score yourself 0-5: erasure (block 1) and laziness (blocks 2, 5) are the");
        System.out.println("two ideas that actually explain WHY Streams behave the way they do.");
    }
}
