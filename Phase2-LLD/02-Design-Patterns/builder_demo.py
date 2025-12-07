"""
Day 8: Builder Pattern Demo
Scenario: A Custom SQL Query Builder.
This shows how to construct a complex string (SQL) step-by-step.
"""

# ==========================================
# 1. The Product (Complex Object)
# ==========================================
class SQLQuery:
    def __init__(self):
        self.table = ""
        self.columns = []
        self.where_clauses = []
        self.limit_count = None
    
    def __str__(self):
        if not self.table:
            return "Invalid Query: Missing Table"
        
        col_str = ", ".join(self.columns) if self.columns else "*"
        query = f"SELECT {col_str} FROM {self.table}"
        
        if self.where_clauses:
            query += " WHERE " + " AND ".join(self.where_clauses)
            
        if self.limit_count is not None:
            query += f" LIMIT {self.limit_count}"
            
        return query + ";"

# ==========================================
# 2. The Builder
# ==========================================
class QueryBuilder:
    def __init__(self):
        self._query = SQLQuery()
    
    def from_table(self, table_name):
        self._query.table = table_name
        return self # Return self for method chaining (Fluent Interface)
    
    def select(self, *columns):
        self._query.columns.extend(columns)
        return self
    
    def where(self, condition):
        self._query.where_clauses.append(condition)
        return self
    
    def limit(self, count):
        self._query.limit_count = count
        return self
    
    def build(self):
        return self._query

# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    print("--- Builder Pattern Demo: SQL Generator ---\n")

    # 1. Simple Query
    # Note how readable the construction is:
    q1 = (QueryBuilder()
          .from_table("users")
          .select("id", "username")
          .build())
    
    print(f"Query 1: {q1}")

    # 2. Complex Query
    q2 = (QueryBuilder()
          .from_table("orders")
          .select("order_id", "total", "date")
          .where("total > 100")
          .where("status = 'PAID'")
          .limit(50)
          .build())
    
    print(f"Query 2: {q2}")

    # 3. Dynamic Construction
    # Builder is great when you don't know the params upfront
    filters = {"age > 18", "country = 'US'"}
    builder = QueryBuilder().from_table("analytics")
    
    for f in filters:
        builder.where(f)
        
    print(f"Query 3: {builder.build()}")
