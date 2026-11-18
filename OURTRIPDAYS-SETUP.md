# @ourtripdays 트렌드 뷰어

## 운영 방식

AI 오피스와 별도 웹으로 운영하고 오피스에서 링크로 여는 구성을 권장한다. Python 수집은 외부 요청·썸네일 메모리를 사용하므로 릴스 렌더러/글쓰기와 한 서버로 합치지 않는다. GitHub Pages는 정적 파일만 제공하므로 PC가 꺼져도 열리지만 검색·계정 수정은 로컬 버전에서 한다. Pages는 공개 사이트이며 가족 사진·개인 메모·토큰은 넣지 않는다.

메인 색 #E0668F와 @ourtripdays 제목, 기존 레이아웃 유지. 유튜브·쇼츠 카테고리 5개, 각 검색어 4~5개는 server.py CATEGORIES에서 관리. 릴스 여행 8개+재테크 10개는 reels_accounts.json에 저장, 기본값도 동일. Nungle은 nungle로 정규화했으며 계정의 실제 존재·조회 성공은 별도 확인 대상이다.

## GitHub Pages 설정 순서

1. GitHub boboomi/daily-trend-viewer Fork를 연다.
2. Actions에서 Fork의 워크플로 실행이 비활성이라면 활성화한다.
3. Settings → Pages → Build and deployment → Source를 GitHub Actions로 선택한다.
4. Actions → 트렌드 수집 및 Pages 배포 → Run workflow → main으로 첫 배포를 실행한다.
5. build-deploy 성공 후 https://boboomi.github.io/daily-trend-viewer/ 를 연다.
6. 이후 매일 오전 7시에 자동 수집한다. 계정·키워드 수정 커밋은 다음 예약에 반영되며 즉시 반영하려면 Run workflow를 사용한다.

## 시간

- 매일 07:00 KST = 전날 22:00 UTC: `0 22 * * *`
- 오늘 2026-11-18 15:00 KST = 2026-11-18 06:00 UTC: `0 6 18 11 *`
- cron에는 연도가 없으므로 schedule-check가 UTC 날짜 2026-11-18인 경우에만 오늘용 수집·배포를 허용한다. 다음 해에는 검사만 실행되고 수집·배포는 건너뛴다. 오늘 실행 후 이 임시 cron 줄을 제거해도 된다.
- push 자동 실행은 제거했다. 첫 확인용 수동 실행 외 정기 수집은 하루 한 번이다. GitHub 대기열 때문에 실행 지연 또는 누락 가능성이 있다.

## 제한

릴스 수집은 외부 서비스 제한으로 비어 있을 수 있다. 등록한 계정 수와 수집 성공한 계정 수는 다르다. 이전 릴스 스냅샷을 재사용할 때도 현재 등록한 계정의 자료만 표시한다. 인기순 검색 결과가 개인적인 추천 적합도를 보장하지는 않는다.

원본 저장소 출처: https://github.com/lmorejh/daily-trend-viewer . 원본 코드와 Git 이력 유지. 별도 라이선스가 확인되지 않은 경우 독자적인 상업 재배포 허용으로 해석하지 않는다.
