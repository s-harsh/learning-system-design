# Schema Design: The Backbone of LLD 🗄️

## 1. Core Concept: Entity-Relationship (ER) Modeling
System design begins by modeling the "Universe of Discourse"—the set of real-world objects and their interactions that the system must represent. We use **ER Diagrams** to visualize this structure before writing any SQL.

### Terminology:
*   **Entity**: A distinct object or concept in the domain (e.g., `User`, `Order`). Represents a table.
*   **Attribute**: A property or characteristic of an entity (e.g., `email`, `price`). Represents a column.
*   **Relationship**: An association between two or more entities (e.g., `User` *places* `Order`). Represents a Foreign Key.

### Cardinality (The Constraints):
Defining *how many* instances of Entity A interact with Entity B is critical for table structure.
1.  **One-to-One (1:1)**: An instance of A is associated with at most one B.
    *   *Implementation*: Unique Foreign Key on either table.
2.  **One-to-Many (1:N)**: An instance of A is associated with multiple B's.
    *   *Implementation*: Foreign Key on the "Many" side (B) pointing to "One" side (A).
3.  **Many-to-Many (M:N)**: Multiple A's interact with multiple B's.
    *   *Implementation*: Requires a **Join Table** (Associative Entity) containing Foreign Keys from both.

---

## 2. Normalization Theory
Normalization is the formal process of organizing data to reduce **Redundancy** and improve **Data Integrity**.
Without specific rules (Normal Forms), databases suffer from **Anomalies**:
*   **Update Anomaly**: Updating data in one place leaves conflicting stale data elsewhere.
*   **Insertion Anomaly**: Inability to add data because it requires unrelated data to exist (e.g., cannot add an Instructor without a Student).
*   **Deletion Anomaly**: Deleting a record unintentionally causes loss of unrelated data.

### First Normal Form (1NF): Atomicity
**The Rule**: Every column must contain atomic (indivisible) values. No repeating groups or arrays.
*   **Violation**: Storing `["Math", "Science"]` in a `Courses` column.
*   **Solution**: Create a separate row for each value.

### Second Normal Form (2NF): Partial Dependency
**The Rule**: The table must be in 1NF, and all non-key attributes must depend on the **Entire Primary Key**.
*   **Violation**: In a table with a composite key `(Student_ID, Course_ID)`, storing `Course_Fee` violates 2NF because `Course_Fee` depends only on `Course_ID`, not `Student_ID`.
*   **Solution**: Move `Course_Fee` to a separate `Courses` table.

### Third Normal Form (3NF): Transitive Dependency
**The Rule**: The table must be in 2NF, and non-key attributes must not depend on other non-key attributes. ("All columns depend on the Key, the whole Key, and nothing but the Key").
*   **Violation**: A `Students` table containing `Instructor_Name` and `Instructor_Phone`. The Phone depends on the name, not the Student.
*   **Solution**: Move Instructor data to an `Instructors` table and reference it via Foreign Key.

---

## 3. Practical Example: University System 🎓

### The Un-Normalized Chaos (0NF)
| Student | Courses | Instructor | Instructor_Phone |
| :--- | :--- | :--- | :--- |
| Harsh | Math, Physics | Dr. Smith | 555-0199 |

### Applying 1NF (Atomic Rows)
| Student | Course | Instructor | Instructor_Phone |
| :--- | :--- | :--- | :--- |
| Harsh | Math | Dr. Smith | 555-0199 |
| Harsh | Physics | Dr. Jones | 555-0200 |

### Applying 2NF & 3NF (Separation of Concerns)
We split this into normalized tables to eliminate redundancy.

**Table 1: Students**
| ID | Name |
| :--- | :--- |
| 1 | Harsh |

**Table 2: Instructors** (Removed Transitive Dependency)
| ID | Name | Phone |
| :--- | :--- | :--- |
| 101 | Dr. Smith | 555-0199 |
| 102 | Dr. Jones | 555-0200 |

**Table 3: Courses**
| ID | Name | Instructor_ID (FK) |
| :--- | :--- | :--- |
| 10 | Math | 101 |
| 11 | Physics | 102 |

**Table 4: Enrollments** (Join Table for M:N)
| Student_ID | Course_ID |
| :--- | :--- |
| 1 | 10 |
| 1 | 11 |

---

## 4. ACID Properties (Data Integrity)
Relational databases guarantee validity through **ACID**:

1.  **Atomicity**: Transactions are "All or Nothing". If a power failure occurs halfway through a money transfer, the entire transaction is rolled back.
2.  **Consistency**: The database always transitions from one valid state to another, strictly adhering to all constraints (Foreign Keys, Unique checks).
3.  **Isolation**: Concurrent transactions do not interfere with each other. (Read `Dirty Reads` vs `Serializable`).
4.  **Durability**: Committed data is permanent and survives system crashes (Write-Ahead Logging).
