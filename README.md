## 2023 DB 텀프로젝트

**Rebase 과정**

1. 같이 작업하고 있는 base에서 팀원의 PR이 머지됨
2. 현재 나의 branch(로컬)에서 작업한 것 → 커밋(커밋이 있을 경우)
3. `git switch base` (base 브랜치로 이동)
4. `git pull origin base` (머지된 변경사항을 base로 가져옴)
5. `git switch stem` (본인 브랜치로 이동)
6. `git rebase base` (base와 rebase 실시)
7. conflict 수정(만약 상대방의 코드 수정시 DM)
8. conflict 해결
9. `git add <file>`
10. `git rebase —continue`
11. 작업을 계속 수행한 뒤 → PR

rebase test
