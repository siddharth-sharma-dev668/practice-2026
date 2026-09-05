/**
 * Week 1 Monday drill - Java companion to gotchas.py. Predict, THEN run, then compare.
 *
 * Run with: java Gotchas.java   (JDK 11+ runs a single .java file directly, no javac step)
 *
 * This targets the one real soft spot in your Java & Spring diagnostic (17/20):
 * Collections scored 3/4. Blocks 1, 2, 4 and 6 below are exactly that gap -
 * measured live, the same protocol as the Python file, not recalled from memory.
 */
import java.util.*;

public class Gotchas {
    public static void main(String[] args) {

        System.out.println("=== 1. ArrayList.get(i) vs LinkedList.get(i) - measured, not memorized ===");
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
        System.out.printf("ArrayList: %.2fms   LinkedList: %.2fms   ratio: %.0fx%n",
            arrayNs / 1e6, linkedNs / 1e6, (double) linkedNs / arrayNs);
        System.out.println("why: ArrayList indexes a backing array directly, O(1) regardless of which");
        System.out.println("     index. LinkedList.get() walks node-by-node from whichever end is closer -");
        System.out.println("     get(0) or get(size-1) is nearly free, but a MIDDLE index (used here, so");
        System.out.println("     this isn't accidentally flattered) is genuinely O(n). get(i) in a loop is");
        System.out.println("     the wrong reason to reach for LinkedList either way.\n");

        System.out.println("=== 2. HashSet.contains O(1) avg vs List.contains O(n) ===");
        Set<Integer> set = new HashSet<>(arrayList);
        t0 = System.nanoTime();
        for (int i = 0; i < 5000; i++) arrayList.contains(n - 1);
        long listNs = System.nanoTime() - t0;
        t0 = System.nanoTime();
        for (int i = 0; i < 5000; i++) set.contains(n - 1);
        long setNs = System.nanoTime() - t0;
        System.out.printf("List.contains: %.2fms   HashSet.contains: %.2fms   ratio: %.0fx%n",
            listNs / 1e6, setNs / 1e6, (double) listNs / setNs);
        System.out.println("why: List.contains scans; HashSet hashes straight to the bucket. Same shape as");
        System.out.println("     the Python list-vs-set check in gotchas.py block 5, different syntax.\n");

        System.out.println("=== 3. ConcurrentModificationException - not actually about threads ===");
        List<Integer> toEdit = new ArrayList<>(List.of(1, 2, 3, 4, 5));
        try {
            for (int x : toEdit) {
                if (x == 3) toEdit.remove(Integer.valueOf(x));
            }
            System.out.println("no exception - list is now: " + toEdit);
        } catch (ConcurrentModificationException e) {
            System.out.println("ConcurrentModificationException: " + e);
        }
        System.out.println("why: removing from a List mid for-each invalidates the iterator's modCount");
        System.out.println("     check. One thread triggers this despite the name - use iterator.remove()");
        System.out.println("     or removeIf() instead.\n");

        System.out.println("=== 4. hashCode contract - mutate a field it depends on, and the set forgets you ===");
        class Point {
            int x;
            Point(int x) { this.x = x; }
            @Override public int hashCode() { return Integer.hashCode(x); }
            @Override public boolean equals(Object o) { return o instanceof Point p && p.x == x; }
        }
        Point p = new Point(5);
        Set<Point> points = new HashSet<>();
        points.add(p);
        System.out.println("contains before mutation: " + points.contains(p));
        p.x = 99;
        System.out.println("contains after mutation:  " + points.contains(p));
        System.out.println("why: HashSet located the bucket using the OLD hashCode. After mutating x, p");
        System.out.println("     now hashes to a different bucket than the one it's actually stored in -");
        System.out.println("     it's stranded. Never mutate a field hashCode()/equals() depend on.\n");

        System.out.println("=== 5. Comparator chaining - multi-key, stable sort ===");
        record Person(String name, int age) {}
        List<Person> people = new ArrayList<>(List.of(
            new Person("sid", 27), new Person("ana", 27), new Person("bo", 19)));
        people.sort(Comparator.comparingInt(Person::age).reversed().thenComparing(Person::name));
        System.out.println(people);
        System.out.println("why: chaining reads left-to-right, same idea as Python's tuple-key sort - age");
        System.out.println("     descending, then name ascending. Java's sort is stable too (TimSort).\n");

        System.out.println("=== 6. ArrayDeque O(1) at both ends vs ArrayList.remove(0) O(n) ===");
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
        System.out.printf("ArrayList.remove(0): %.2fms   ArrayDeque.removeFirst(): %.2fms%n",
            listFrontNs / 1e6, dequeFrontNs / 1e6);
        System.out.println("why: ArrayList.remove(0) shifts every remaining element left, O(n). ArrayDeque");
        System.out.println("     is a resizable array used as a ring buffer - O(1) at either end.\n");

        System.out.println("=== Self-check ===");
        System.out.println("Score yourself 0-6: your diagnostic scored Collections 3/4 - blocks 1, 2, 4");
        System.out.println("and 6 above are exactly that gap, measured instead of recalled.");
    }
}
