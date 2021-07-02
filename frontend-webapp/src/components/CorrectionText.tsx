import React from 'react'
import { Correction } from '../interfaces/interfaces'

interface CorrectionProps {
  text: string
  correction: Correction
  isSelected: boolean
  setSelectedCorrection(correction: Correction): void
}

export default function Correction({
  text,
  correction,
  isSelected,
  setSelectedCorrection
}: CorrectionProps) {
  return (
    <span
      className={`Correction${isSelected ? ' Selected' : ''}`}
      onClick={() => setSelectedCorrection(correction)}
      title={correction.short_message || correction.message}
    >
      {text}
    </span>
  )
}
