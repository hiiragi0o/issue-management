# issue-management
 業務で発生する案件の進捗を、複数名で効率的に管理するためのWebアプリケーションです。 <br >
 ユーザーはアカウントを作成し、同一案件に対してコメントやステータス更新を通じて共同管理が可能です。 <br >

<img src="https://github.com/user-attachments/assets/8a738383-21c1-4472-b38f-d9bbe91f618d" width="600">

<kbd><img src="https://github.com/user-attachments/assets/d036f7d6-70b6-43e1-a0c7-f4a25c54e8f4" width="1000"></kbd>

<kbd><img src="https://github.com/user-attachments/assets/86d05a99-9957-4339-b945-0304750aad6a" width="800"></kbd>

# URL
 https://issue-management.onrender.com <br >
 画面下部に記載のアカウントから、ログインできます。


# 使用技術
- Python 3.8.10
- Django 4.2.18
- JavaScript
- Bootstrap 5.3
- AWS S3（ファイルアップロード）
- Render（本番環境デプロイ）
- Google Apps Script（通知処理やデータ自動化など補助機能として活用）
  

# 機能一覧
- ユーザー登録、ログイン
- 案件の新規登録・編集・削除
- 案件検索
- コメント投稿・編集・削除
- ファイルアップロード機能(AWS S3)
- ページネーション

 <br > 

# 作成の背景
 もとは病院内での案件管理を効率化するために、FileMaker（ローコード開発ソフト）で独学で作成し、実務運用していたアプリです。 <br >
 Python, Djangoで再構築および機能改善しました。

# FileMaker 時代からの改善ポイントや工夫
**改善したUI/UX**
- 進捗入力欄をユーザーごと、入力日時ごとのコメント投稿に変更
- 投稿日時の自動記録で情報の信頼性向上
- 自分のコメントのみ編集・削除可能
  
**認証・権限管理**
- Djangoでログイン機能を実装し、認証管理を導入
 
**検索・表示機能の改善**
- 検索結果にページネーションを追加し、閲覧性を向上
- 案件URLをワンクリックでコピーできる共有機能を実装
 
**外部連携・補助機能**
- ファイルアップロード機能（AWS S3）を追加
- ログインやコメント時の通知をプッシュ表示（Django + Bootstrap）
- Render（本番環境デプロイ）
- Google Apps Script（GAS）を使って、Render上のポートフォリオに定期的にHTTPリクエストを送信し、スリープ状態への移行を防止

