# 個人開発 収益化Skill集 for Claude Code(非公式)— Lite版

個人開発の「作って売る」工程をClaude Codeに任せるためのAgent Skill集の**無料版**です。仕様化とローンチ点検の2つのSkillを収録しています。このまま実務で使えます。

> **非公式表記:** 本Skill集は個人が作成した非公式コンテンツであり、Anthropic社およびClaude Code公式とは一切関係ありません。Claude / Claude CodeはAnthropic社の製品です。

- バージョン: v0.1.2 / ライセンス: `LICENSE.md`(再配布・転売のみ禁止。利用・改変・成果物の商用利用は自由)

## このリポジトリに含まれるもの

```
├── README.md    ← このファイル
├── LICENSE.md   ← 利用規約・免責
└── skills/
    ├── idea-to-spec/SKILL.md
    └── launch-checklist/SKILL.md
```

## 収録Skill(2個)

| Skill | 役割 |
|---|---|
| `idea-to-spec` | アイデアを1〜2週間で作れるMVP仕様書に変換(ユーザーストーリー5本・やらないことリスト・リスクフラグ付き) |
| `launch-checklist` | 公開/販売前の最終点検(法務表記・誇大表現・決済・サポート導線をOK/NG/不明で判定) |

## 導入手順

1. このリポジトリをclone(またはzipダウンロード)
2. `skills/` 配下を、利用プロジェクトの `.claude/skills/` にコピー
   ```bash
   mkdir -p .claude/skills
   cp -r skills/* .claude/skills/
   ```
3. Claude Codeで「◯◯を作りたいので仕様にして」「公開前チェックして」と話しかける

Claude Code以外のAIでも、SKILL.md本文を貼り付ければそのまま動きます(自己完結型)。

## 使い方の例

```
あなた: 読書メモをAIで整理するアプリを作りたい。仕様にして
→ idea-to-spec が発動し、MVP仕様書(5ストーリー/やらないこと/リスク/14日計画)が出ます

あなた: 明日、有料noteを公開する。チェックして
→ launch-checklist が発動し、判定表とブロッカー一覧が出ます
```

## Lite版とPro版の違い

Lite版は「何を作るか決める(仕様化)」と「公開前に事故を防ぐ(点検)」の入口と出口をカバーしており、この2つだけで完結して使えます。

その間の工程まで任せたい方向けに、Pro版があります。Pro版は**仕様化→実装雛形→監査→販売文→販売ページ診断→記事→点検まで一気通貫**の全7 Skill+サンプルレポート2本(監査/診断の出力例)のセットです。必要になったタイミングでどうぞ。

| 工程 | Lite | Pro |
|---|---|---|
| 仕様化(idea-to-spec) | ✅ | ✅ |
| 実装雛形(Next.js+Supabase+Stripe) | – | ✅ |
| 公開前監査(重大度・証拠付きレポート) | – | ✅ |
| 販売文・LP・FAQ(誇大表現なし設計) | – | ✅ |
| note/Zenn記事作成 | – | ✅ |
| 販売ページ診断(50点採点・Before/After) | – | ✅ |
| ローンチ点検(launch-checklist) | ✅ | ✅ |

Pro版は現在準備中です。公開時にこのREADMEと制作者のZenn/Xで告知します(本リポジトリはLite版単体で完結して使えます)。

## 免責

本Skill集は制作・販売準備の効率化を目的とした補助ツールであり、収益・成果・適法性・安全性を保証するものではありません。詳細は `LICENSE.md` を参照してください。
