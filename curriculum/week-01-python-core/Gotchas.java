/**
 * Week 1 Monday drill - Java companion to gotchas.py.
 *
 * HOW TO USE THIS FILE: run `java Gotchas.java` (JDK 11+ runs a single .java
 * file directly, no javac step). The terminal shows you code and ASKS a
 * question, then waits. Type anything - your guess, "no idea" - and press
 * Enter. The real answer prints right after, with a "why".
 *
 * This targets the one real soft spot in your Java & Spring diagnostic (17/20):
 * Collections scored 3/4. Blocks 1, 2, 4 and 6 below are exactly that gap -
 * measured live, the same protocol as the Python file, not recalled from memory.
 */
import java.util.*;

public class Gotchas {
    static Scanner scanner = new Scanner(System.in);

    static void predict(int blockNum, String title, String codeShown, String question) {
        System.out.println();
        System.out.println("=".repeat(70));
        System.out.println("BLOCK " + blockNum + ": " + title);
        System.out.println("=".repeat(70));
        System.out.println("CODE:");
        for (String line : codeShown.split("\n")) System.out.println("    " + line);
        System.out.println();
        System.out.println("QUESTION: " + question);
        System.out.print(">>> Type your guess, then press Enter to reveal the real answer: ");
        scanner.nextLine();
        System.out.println();
    }

    static void reveal(String... lines) {
        System.out.println("ACTUAL ANSWER:");
        for (String line : lines) System.out.println("    " + line);
        System.out.println();
    }

    public static void main(String[] args) {

        predict(1, "ArrayList.get(i) vs LinkedList.get(i) - measured, not memorized",
            "arrayList.get(mid);   vs   linkedList.get(mid);   // mid = a MIDDLE index, not an end",
            "Which is faster, and roughly how much - 2x? 10x? 100x? Guess a number.");
        int n = 20000;
        List<Integer> arrayList = new ArrayList<>();
        List<Integer> linkedList = new LinkedList<>();
        for (int i = 0; i < n; i++) { arrayList.add(i); linkedList.add(i); }
        int mid = n / 2;
        long t0 = System.nanoTime();
        for (int i = 0; i < 5000; i++) arrayList.get(mid);
        long arrayNs = System.nanoTime() - t0;
        t0 = System.nanoTime();
        for (int i = 0; i < 5000; i++) linkedList.get(mid);
        long linkedNs = System.nanoTime() - t0;
        reveal(String.format("ArrayList: %.2fms   LinkedList: %.2fms   ratio: %.0fx",
            arrayNs / 1e6, linkedNs / 1e6, (double) linkedNs / arrayNs));
        System.out.println("why: ArrayList indexes a backing array directly, O(1) regardless of which");
        System.out.println("     index. LinkedList.get() walks node-by-node from whichever end is closer -");
        System.out.println("     get(0) or get(size-1) is nearly free, but a MIDDLE index (used here, so");
        System.out.println("     this isn't accidentally flattered) is genuinely O(n). get(i) in a loop is");
        System.out.println("     the wrong reason to reach for LinkedList either way.\n");

        predict(2, "HashSet.contains O(1) avg vs List.contains O(n)",
            "arrayList.contains(x);   vs   set.contains(x);   // same 20,000 elements",
            "Same shape of question as block 1. Which is faster, and roughly how much?");
        Set<Integer> set = new HashSet<>(arrayList);
        t0 = System.nanoTime();
        for (int i = 0; i < 5000; i++) arrayList.contains(n - 1);
        long listNs = System.nanoTime() - t0;
        t0 = System.nanoTime();
        for (int i = 0; i < 5000; i++) set.contains(n - 1);
        long setNs = System.nanoTime() - t0;
        reveal(String.format("List.contains: %.2fms   HashSet.contains: %.2fms   ratio: %.0fx",
            listNs / 1e6, setNs / 1e6, (double) listNs / setNs));
        System.out.println("why: List.contains scans; HashSet hashes straight to the bucket. Same shape as");
        System.out.println("     the Python list-vs-set check in gotchas.py block 5, different syntax.\n");

        predict(3, "ConcurrentModificationException - not actually about threads",
            "List<Integer> toEdit = [1,2,3,4,5];\nfor (int x : toEdit) { if (x == 3) toEdit.remove(x); }",
            "Does this loop finish quietly, or throw an exception? If it throws, what kind?");
        List<Integer> toEdit = new ArrayList<>(List.of(1, 2, 3, 4, 5));
        try {
            for (int x : toEdit) {
                if (x == 3) toEdit.remove(Integer.valueOf(x));
            }
            reveal("no exception - list is now: " + toEdit);
        } catch (ConcurrentModificationException e) {
            reveal("ConcurrentModificationException: " + e);
        }
        System.out.println("why: removing from a List mid for-each invalidates the iterator's modCount");
        System.out.println("     check. One thread triggers this despite the name - use iterator.remove()");
        System.out.println("     or removeIf() instead.\n");

        predict(4, "hashCode contract - mutate a field it depends on",
            "Point p = new Point(5);\nset.add(p);\np.x = 99;   // mutate AFTER adding\nset.contains(p);  // ?",
            "Point's hashCode is based on x. Once p.x changes to 99, does set.contains(p) still say true?");
        class Point {
            int x;
            Point(int x) { this.x = x; }
            @Override public int hashCode() { return Integer.hashCode(x); }
            @Override public boolean equals(Object o) { return o instanceof Point p && p.x == x; }
        }
        Point p = new Point(5);
        Set<Point> points = new HashSet<>();
        points.add(p);
        String before = "contains before mutation: " + points.contains(p);
        p.x = 99;
        String after = "contains after mutation:  " + points.contains(p);
        reveal(before, after);
        System.out.println("why: HashSet located the bucket using the OLD hashCode. After mutating x, p");
        System.out.println("     now hashes to a different bucket than the one it's actually stored in -");
        System.out.println("     it's stranded. Never mutate a field hashCode()/equals() depend on.\n");

        predict(5, "Comparator chaining - multi-key, stable sort",
            "people = [(sid,27), (ana,27), (bo,19)]\n"
            + "people.sort(Comparator.comparingInt(Person::age).reversed().thenComparing(Person::name));",
            "What order do the three people come out in?");
        record Person(String name, int age) {}
        List<Person> people = new ArrayList<>(List.of(
            new Person("sid", 27), new Person("ana", 27), new Person("bo", 19)));
        people.sort(Comparator.comparingInt(Person::age).reversed().thenComparing(Person::name));
        reveal(people.toString());
        System.out.println("why: chaining reads left-to-right, same idea as Python's tuple-key sort - age");
        System.out.println("     descending, then name ascending. Java's sort is stable too (TimSort).\n");

        predict(6, "ArrayDeque O(1) at both ends vs ArrayList.remove(0) O(n)",
            "frontList.remove(0);   vs   deque.removeFirst();   // 8000 times each, same starting data",
            "Same shape of question as blocks 1 and 2, this time at the FRONT. Which wins, roughly how much?");
        Deque<Integer> deque = new ArrayDeque<>(arrayList);
        List<Integer> frontList = new ArrayList<>(arrayList);
        t0 = System.nanoTime();
        for (int i = 0; i < 8000; i++) {
            if (!frontList.isEmpty()) frontList.remove(0); else frontList.add(0, 0);
        }
        long listFrontNs = System.nanoTime() - t0;
        t0 = System.nanoTime();
        for (int i = 0; i < 8000; i++) {
            if (!deque.isEmpty()) deque.removeFirst(); else deque.addFirst(0);
        }
        long dequeFrontNs = System.nanoTime() - t0;
        reveal(String.format("ArrayList.remove(0): %.2fms   ArrayDeque.removeFirst(): %.2fms",
            listFrontNs / 1e6, dequeFrontNs / 1e6));
        System.out.println("why: ArrayList.remove(0) shifts every remaining element left, O(n). ArrayDeque");
        System.out.println("     is a resizable array used as a ring buffer - O(1) at either end.\n");

        System.out.println();
        System.out.println("=".repeat(70));
        System.out.println("SELF-CHECK");
        System.out.println("=".repeat(70));
        System.out.println("Score yourself 0-6: your diagnostic scored Collections 3/4 - blocks 1, 2, 4");
        System.out.println("and 6 above are exactly that gap, measured instead of recalled.");
    }
}
