import heapq

def solution(book_time):
    answer = 0
    heap = []
    book = []
    for b in book_time:
        h1, m1 = map(int, b[0].split(':'))
        h2, m2 = map(int, b[1].split(':'))
        book.append((h1 * 60 + m1, h2 * 60 + m2 + 10))
        
    book.sort(key=lambda x: x[0])
    
    for b in book:
        while heap and heap[0] <= b[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, b[1])
        answer = max(answer, len(heap))
    
    return answer