import React, { ReactNode } from 'react'
import { Correction } from '../interfaces/interfaces'

interface CorrectionHighligherProps {
  text: string
  corrections: Correction[]
  selectedCorrection: Correction
  setSelectedCorrection(correction: Correction): void
}

export default function CorrectionHighlighter({
  text,
  corrections,
  selectedCorrection,
  setSelectedCorrection
}: CorrectionHighligherProps) {
  if (!corrections.length) {
    return null
  }

  // Sort corrections by start offset
  const sortedCorrections = [...corrections].sort((a, b) => a.offset - b.offset)

  const nodes: ReactNode[] = []

  // Add any text before the first correction.
  if (sortedCorrections[0].offset > 0) {
    nodes.push(text.slice(0, sortedCorrections[0].offset))
  }

  for (let i = 0; i < sortedCorrections.length; i += 1) {
    const correction = sortedCorrections[i]
    const offset = correction.offset
    const end = offset + correction.length

    nodes.push(
      <span
        className={`Correction ${
          selectedCorrection === correction ? 'Selected' : ''
        }`}
        onClick={() => setSelectedCorrection(correction)}
      >
        {text.slice(offset, end)}
      </span>
    )

    // Add any text after the correction.
    const nextIndex =
      i < sortedCorrections.length - 1
        ? sortedCorrections[i + 1].offset
        : text.length
    if (nextIndex > end) {
      nodes.push(text.slice(end, nextIndex))
    }
  }

  return <span className="CorrectedLine">{nodes}</span>
}
