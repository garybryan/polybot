import { render, screen } from '@testing-library/react'
import React from 'react'
import { Correction } from '../interfaces/interfaces'
import ChatLineCorrection from './ChatLineCorrection'
import Corrections from './Corrections'

describe('ChatLineCorrection', () => {
  const language = 'en-GB'
  const user = 'mock user'
  const text = 'mock text'
  const corrections = [
    {
      message: 'message',
      suggestions: [],
      offset: 0,
      length: 6,
      context: {},
      rule: {},
      sentence: 'sentence',
    },
  ]
  const correctionsEmpty: Correction[] = []

  it('Renders corrections if there are corrections', () => {
    render(
      <ChatLineCorrection
        language={language}
        user={user}
        text={text}
        corrections={corrections}
      />
    )
    expect(screen.getByTestId('corrections')).toBeInTheDocument()
  })

  it('Does not render corrections if there are no corrections', () => {
    render(
      <ChatLineCorrection
        language={language}
        user={user}
        text={text}
        corrections={correctionsEmpty}
      />
    )
    expect(screen.queryByTestId('corrections')).not.toBeInTheDocument()
    expect(screen.getByText('Looks good!')).toBeInTheDocument()
  })
})
