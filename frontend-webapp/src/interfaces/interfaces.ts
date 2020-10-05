export interface Line {
  language: string
}

export interface UserLine extends Line {
  user: string
}

export interface TextLine extends UserLine {
  text: string
}

export interface Suggestion {
  value: string
  short_description?: string
}

export interface Correction {
  message: string
  short_message?: string
  suggestions: Suggestion[]
  offset: number
  length: number
  context: object
  rule: object
  sentence: string
}

export interface CorrectionLine extends UserLine {
  corrections: Correction[]
}

export type LogLine = TextLine | CorrectionLine
