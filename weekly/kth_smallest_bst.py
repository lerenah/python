class Solution(object):
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
