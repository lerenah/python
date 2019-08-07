class Solution(object):

    # faster
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        collection = []

        def helper(node):
            if node is None:
                return
            helper(node.left)
            collection.append(node.val)
            helper(node.right)
        helper(root)
        return collection[k-1]

        # slower solution
        def kthSmallest(self, root, k):
            """
            :type root: TreeNode
            :type k: int
            :rtype: int
            """
            import heapq
            collection = []

            def helper(node):
                if node is None:
                    return
                helper(node.left)
                helper(node.right)
                collection.append(node.val)

            helper(root)
            heapq.heapify(collection)
            return heapq.nsmallest(k, collection)[-1]
