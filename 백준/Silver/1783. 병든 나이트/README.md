# [Silver III] 병든 나이트 - 1783 

[문제 링크](https://www.acmicpc.net/problem/1783) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현, 그리디 알고리즘, 많은 조건 분기

### 제출 일자

2025년 7월 12일 18:26:10

### 문제 설명

<p>병든 나이트가 N × M 크기 체스판의 가장 왼쪽아래 칸에 위치해 있다. 병든 나이트는 건강한 보통 체스의 나이트와 다르게 4가지로만 움직일 수 있다.</p>

<ol>
	<li>2칸 위로, 1칸 오른쪽</li>
	<li>1칸 위로, 2칸 오른쪽</li>
	<li>1칸 아래로, 2칸 오른쪽</li>
	<li>2칸 아래로, 1칸 오른쪽</li>
</ol>

<p>병든 나이트는 여행을 시작하려고 하고, 여행을 하면서 방문한 칸의 수를 최대로 하려고 한다. 병든 나이트의 이동 횟수가 4번보다 적지 않다면, 이동 방법을 모두 한 번씩 사용해야 한다. 이동 횟수가 4번보다 적은 경우(방문한 칸이 5개 미만)에는 이동 방법에 대한 제약이 없다.</p>

<p>체스판의 크기가 주어졌을 때, 병든 나이트가 여행에서 방문할 수 있는 칸의 최대 개수를 구해보자.</p>

### 입력 

 <p>첫째 줄에 체스판의 세로 길이 N와 가로 길이 M이 주어진다. N과 M은 2,000,000,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>병든 나이트가 여행에서 방문할 수 있는 칸의 개수중 최댓값을 출력한다.</p>

