from collections import defaultdict, namedtuple

# Define a namedtuple for the FP-Tree nodes
class FPNode:
    def __init__(self, item, count, parent):
        self.item = item  # Item name
        self.count = count  # Count of occurrences of this item in transactions
        self.parent = parent  # Parent node in the FP-Tree
        self.children = {}  # Children nodes in the FP-Tree

# FP-Growth Algorithm implementation
class FPGrowth:
    def __init__(self, min_support):
        self.min_support = min_support  # Minimum support threshold
        self.item_counts = defaultdict(int)  # Dictionary to store counts of individual items
        self.transactions = []  # List to store transactions
        self.header_table = {}  # Header table for linking nodes of the same item
        self.frequent_itemsets = []  # List to store frequent itemsets

    def fit(self, transactions):
        self.transactions = transactions
        self._calculate_item_counts()
        self._build_fp_tree()

    def _calculate_item_counts(self):
        # Count occurrences of each item
        for transaction in self.transactions:
            for item in transaction:
                self.item_counts[item] += 1

        # Remove items that do not meet minimum support
        self.item_counts = {item: count for item, count in self.item_counts.items() if count >= self.min_support}

    def _build_fp_tree(self):
        # Initialize root of FP-Tree
        self.root = FPNode(item=None, count=None, parent=None)

        # Process each transaction and add it to FP-Tree
        for transaction in self.transactions:
            sorted_items = sorted([item for item in transaction if item in self.item_counts],
                                  key=lambda item: (-self.item_counts[item], item))  # Sort by count and lexicographically

            current_node = self.root
            for item in sorted_items:
                if item in current_node.children:
                    # Increment count of existing node
                    current_node.children[item].count += 1
                else:
                    # Create new node
                    new_node = FPNode(item=item, count=1, parent=current_node)
                    current_node.children[item] = new_node

                    # Update header table
                    if item in self.header_table:
                        last_node = self.header_table[item]
                        while last_node.link:
                            last_node = last_node.link
                        last_node.link = new_node
                    else:
                        self.header_table[item] = new_node

                # Move to the next node
                current_node = current_node.children[item]

    def _find_prefix_paths(self, item):
        # Find all prefix paths in the FP-Tree for a given item
        conditional_patterns = []
        node = self.header_table[item]
        while node:
            prefix_path = []
            current_node = node.parent
            while current_node.item:
                prefix_path.append(current_node.item)
                current_node = current_node.parent
            if prefix_path:
                conditional_patterns.append((prefix_path, node.count))
            node = node.link
        return conditional_patterns

    def _mine_fp_tree(self, prefix=[]):
        # Mine the FP-Tree for frequent itemsets recursively
        for item in self.header_table:
            # Create new frequent itemset
            new_frequent_itemset = prefix + [item]
            self.frequent_itemsets.append(new_frequent_itemset)

            # Generate conditional pattern base
            conditional_patterns = self._find_prefix_paths(item)
            conditional_transactions = []
            for path, count in conditional_patterns:
                for _ in range(count):
                    conditional_transactions.append(path)

            # Create conditional FP-Tree
            conditional_tree = FPGrowth(min_support=self.min_support)
            conditional_tree.fit(conditional_transactions)

            # Mine the conditional FP-Tree recursively
            if conditional_tree.frequent_itemsets:
                conditional_tree._mine_fp_tree(prefix=new_frequent_itemset)

    def generate_frequent_itemsets(self):
        # Mine FP-Tree for frequent itemsets
        self.frequent_itemsets = []
        self._mine_fp_tree()
        return self.frequent_itemsets


# Example usage:
if __name__ == "__main__":
    # Example transactions
    transactions = [
        ['K', 'E', 'M', 'O', 'Y'],
        ['K', 'E', 'O', 'Y'],
        ['K', 'M', 'Y'],
        ['K', 'E', 'M'],
        ['K', 'E', 'O']
    ]

    # Minimum support count
    min_support = 2

    # Create FP-Growth object
    fp_growth = FPGrowth(min_support=min_support)

    # Fit the model with transactions
    fp_growth.fit(transactions)

    # Generate frequent itemsets
    frequent_itemsets = fp_growth.generate_frequent_itemsets()

    # Print frequent itemsets
    print("Frequent Itemsets:")
    for itemset in frequent_itemsets:
        print(itemset)
