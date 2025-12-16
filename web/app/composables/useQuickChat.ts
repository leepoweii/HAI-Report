/**
 * Quick Chat Composable
 * 提供隨機輪播的快速問題按鈕
 */

const allQuestions = [
  // === 基本操作 ===
  '如何探索 3D 虛擬世界？',
  '手機怎麼操作？',
  '怎麼切換視角？',

  // === 展覽導覽 ===
  '這個展覽在介紹什麼？',
  '展覽有哪些內容？',
  '二樓有什麼可以看？',
  '樓梯在哪裡？',

  // === 技術與專案 ===
  '這個網站用了什麼技術？',
  '這是誰做的專案？',
  '你是怎麼運作的？',
]

export function useQuickChat() {
  /**
   * 隨機取 n 個問題
   * @param count 要取的問題數量，預設 3
   */
  const getRandomQuestions = (count: number = 3): string[] => {
    const shuffled = [...allQuestions].sort(() => Math.random() - 0.5)
    return shuffled.slice(0, count)
  }

  /**
   * 取得所有問題
   */
  const getAllQuestions = (): string[] => allQuestions

  return {
    allQuestions,
    getRandomQuestions,
    getAllQuestions,
  }
}
