export interface Line {
  language: string
}

export interface UserLine extends Line {
  user: string
}

export interface TextLine extends UserLine {
  text: string
}

export interface CorrectionLine extends UserLine {
  corrections: string[]
}

export type LogLine = TextLine | CorrectionLine

export interface Correction {
  message: string
  short_message: string
  suggestions: object[]
  offset: number
  length: number
  context: object
  rule: object
  sentence: string
}
