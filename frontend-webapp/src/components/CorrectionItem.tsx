import React from 'react'
import { Correction } from '../interfaces/interfaces'

interface CorrectionProperties {
  correction: Correction
}

export default function CorrectionItem({ correction }: CorrectionProperties) {
  return (
    <li>
      <strong>{correction.message}</strong>
      <br />
      Offset {correction.offset}, length {correction.length}
    </li>
  )
}
