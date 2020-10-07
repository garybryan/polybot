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
      Suggestions:
      <ol>
        {correction.suggestions.map((suggestion, index) => (
          <li key={index}>
            <em>{suggestion.value}</em>
            {suggestion.short_description &&
              ` (${suggestion.short_description})`}
          </li>
        ))}
      </ol>
    </li>
  )
}
