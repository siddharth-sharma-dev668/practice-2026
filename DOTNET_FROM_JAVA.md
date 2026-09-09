# .NET basics, translated from Java

Priority 7/10 — mid, not core. The goal here is narrow: pass a .NET-developer screen and first technical round, not become a .NET engineer. Every section below leans on something you already know from Java, because C#/.NET and Java/Spring are close cousins — same OOP roots, same "framework does the wiring" philosophy, mostly different names for the same ideas. Where that's true, this file says so plainly. Where .NET genuinely does something Java doesn't, that's flagged loudly, because that's exactly where a Java-background candidate gets caught off guard.

No SDK is installed on this machine yet, so nothing below is a "run it and see" claim the way the Python/Java drills are — these are stable, well-established language facts, not measured output. When you actually book a .NET interview, say so and this gets upgraded to the same predict-then-run treatment (install the SDK, build real drills, verify every claim).

## 1. The direct name-swaps (say these out loud, they should feel obvious)

| You know this in Java | It's called this in .NET |
|---|---|
| Spring Boot | ASP.NET Core |
| Spring Bean / `@Component` | Service registered in the DI container |
| JPA / Hibernate | Entity Framework Core (EF Core) |
| Maven / `pom.xml` | NuGet / `.csproj` |
| `mvn` | `dotnet` CLI |
| `application.properties` | `appsettings.json` |
| JVM | CLR (Common Language Runtime) |
| `@RestController` + `@GetMapping` | `[ApiController]` + `[HttpGet]` |
| `@Autowired` constructor injection | Constructor injection (same idea, built into the framework, no annotation needed) |
| Streams (`.stream().filter().map()`) | LINQ (`.Where().Select()`) |
| `CompletableFuture` | `Task` + `async`/`await` |
| Checked/unchecked exceptions | Just exceptions — C# has no checked exceptions at all |

If an interviewer says a term from the right column and you blank, mentally substitute the left column first. Most of the time the underlying concept is one you already understand.

## 2. Syntax differences that actually matter

- **Properties are a language feature, not a convention.** In Java you write `getName()`/`setName()` by hand (or Lombok generates them). In C#: `public string Name { get; set; }` — the getter/setter pair IS the field, syntactically. Callers write `person.Name = "Sid"`, not `person.setName("Sid")`.
- **`var` is real type inference**, resolved at compile time (unlike Java's `var`, which is similar — this one actually IS the same idea, just introduced earlier in C#'s history).
- **String interpolation is built in**: `$"Hello {name}"` instead of `"Hello " + name` or `String.format`.
- **Properties/fields default to PascalCase** (`FirstName`, not `firstName`) — the naming convention itself is different, not just style preference; getting this wrong reads as "hasn't actually written C#."
- **Nullable reference types are opt-in but increasingly default in new projects.** `string?` explicitly means "this can be null"; a plain `string` is meant to never be null, and the compiler warns you if you don't check. Java has no equivalent — every object reference is nullable by default, always. This is a genuine mental shift, not just syntax.

## 3. The one truly new concept: value types vs. reference types

This is the biggest trap for a Java-background candidate, because Java simply doesn't have this distinction for anything you'd define yourself.

- In Java, **every object you create lives on the heap and is accessed by reference.** Assigning `b = a` always copies the reference — both names point at the same object. You've drilled this exact fact in `gotchas.py`'s Python equivalent already.
- In C#, a `class` behaves the same way — reference semantics, heap-allocated, `b = a` shares one object.
- But C# also has `struct`, and a `struct` is a **value type**: assigning `b = a` copies the entire struct's data. `b` and `a` are now two completely independent copies. Mutating `b` afterward does NOT affect `a`.

```csharp
struct PointStruct { public int X; }
class PointClass { public int X; }

var s1 = new PointStruct { X = 5 };
var s2 = s1;        // COPY - independent value
s2.X = 99;
// s1.X is still 5

var c1 = new PointClass { X = 5 };
var c2 = c1;        // REFERENCE - same object
c2.X = 99;
// c1.X is now also 99 - same trap as Java's aliasing, this part IS familiar
```

Why this matters in an interview: "when would you use a struct?" is a real, common question. The honest answer — small, immutable, short-lived data (like a 2D point, a money amount, a date range) where copying is cheap and you want to avoid heap allocation/garbage collection pressure. `DateTime`, `decimal`, and all the numeric types in .NET are structs for exactly this reason.

## 4. Garbage collection — same idea, different generations story

Both the JVM and the CLR are generational, tracing garbage collectors — the core idea you already know (unreachable objects get reclaimed, reachability is about GC roots, not manual `free()`) transfers directly. The vocabulary differs slightly: .NET talks about **Gen 0, Gen 1, Gen 2** (young objects collected fast and often in Gen 0; survivors get promoted to Gen 1, then Gen 2 for long-lived objects) plus a separate **Large Object Heap** for big allocations. Conceptually this is the same young-generation/old-generation split the JVM does, just named by number instead of by "young/old."

## 5. Async: `async`/`await` vs `CompletableFuture`

Java's `CompletableFuture` and C#'s `Task` solve the same problem (don't block a thread waiting on I/O), but C#'s `async`/`await` keywords make the calling code read like synchronous code:

```csharp
public async Task<string> GetDataAsync()
{
    var result = await httpClient.GetStringAsync(url);  // yields the thread while waiting
    return result;
}
```

The gotcha interviewers probe for: **`async` doesn't mean "runs on a new thread."** It means "this method can pause and resume without blocking the calling thread while it waits." Mixing `.Result` or `.Wait()` (blocking calls) with `async` code is the classic way to deadlock a .NET application — conceptually similar to why you never call `.get()` on a Java `Future` from inside code that same future depends on, just a sharper, more common footgun in .NET because `async`/`await` makes it so easy to write async code that LOOKS synchronous.

## 6. ASP.NET Core specifics

- **Dependency injection is built into the framework itself** — no separate container library the way Spring needs its own context. You register services in `Program.cs`: `builder.Services.AddScoped<IMyService, MyService>();`
- **Three lifetimes, not Spring's two common ones:**
  - `Singleton` — one instance, ever (same as Spring's default `@Component` scope).
  - `Scoped` — one instance per HTTP request (roughly Spring's request scope).
  - `Transient` — a new instance every single time it's injected, even twice in the same request. Java/Spring doesn't have a direct equivalent to this one by default — it's worth naming as the genuinely new option.
- **Middleware pipeline** is an explicit, ordered list you configure yourself in `Program.cs` (`app.UseAuthentication(); app.UseAuthorization(); app.MapControllers();`) — conceptually the same idea as a Spring filter chain, but the ordering is visibly one line per step instead of configured via annotations/beans.

## 7. EF Core specifics

- **`DbContext`** is your entry point — roughly JPA's `EntityManager`, but you typically define your own subclass listing every table as a `DbSet<T>` property, which is more explicit than JPA's repository-scanning approach.
- **LINQ queries against `DbSet<T>` translate to SQL** — `context.Employees.Where(e => e.Salary > 65000)` becomes a real `WHERE` clause, the same idea as Spring Data JPA method-name queries or JPQL, just written as ordinary C# instead of a separate query language.
- **Migrations** (`dotnet ef migrations add ...`) are the direct equivalent of Flyway/Liquibase-style versioned schema changes — closer to that than to Hibernate's auto-DDL, which is worth mentioning if asked, since "does EF auto-create your schema" is a real interview question and the honest answer is "it can, but migrations are the production-safe path," same as the Hibernate answer.

## 8. Interview question bank (basics-level, matches this file's scope)

1. What's the difference between a `struct` and a `class`? (§3 above — value vs reference semantics, this is the #1 question.)
2. What does `async`/`await` actually do — does it create a new thread? (§5 — no, it frees the calling thread while waiting.)
3. What are the three DI lifetimes in ASP.NET Core, and when would you use `Transient` over `Scoped`? (§6)
4. What's the difference between `IEnumerable<T>` and `IQueryable<T>`? (`IEnumerable` runs in memory once materialized; `IQueryable` builds an expression tree that EF Core translates into SQL — calling `.ToList()` too early is a real performance bug, the C# equivalent of pulling a whole table into Python before filtering it.)
5. What happens if you box a value type? (Boxing wraps a `struct` in a heap-allocated object so it can be treated as `object` — costs an allocation and a copy; unboxing reverses it. This is the .NET-specific performance gotcha interviewers like, roughly analogous to Java's autoboxing `int`→`Integer` cost, which you already have the instinct for.)
6. How does garbage collection work in .NET? (§4 — generational, Gen 0/1/2 + LOH, same underlying idea as the JVM.)
7. What's middleware, and does order matter? (§6 — yes, order is explicit and matters: authentication before authorization, for instance.)
8. `record` vs `class` vs `struct` — when would you use a `record`? (A `record` is reference-type by default but gets free value-based equality and immutability — good for DTOs, similar motivation to Java's `record` type, which you already know from recent Java.)

## Where the Java thread's time goes on a ".NET Saturday"

Pick ONE section above per session, read it against something you already do in Java/Spring, then write 3-4 sentences in your own words comparing them (same "design it first, explain it plainly" habit as everything else in this plan). This file is intentionally light enough to work through without a weekly-generated drill file — upgrade it to real runnable code once an actual .NET interview is on the calendar.
