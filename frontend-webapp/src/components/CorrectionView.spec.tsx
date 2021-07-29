import { render, screen } from '@testing-library/react'
import React from 'react'
import CorrectionView from './CorrectionView'

describe('CorrectionView', () => {
  const correction = {
    message: 'message',
    suggestions: [
      {
        value: 'suggestion 1 value',
      },
      {
        value: 'suggestion 2 value',
        short_description: 'suggestion 2 description',
      },
    ],
    offset: 0,
    length: 6,
    context: {},
    rule: {},
    sentence: 'sentence',
  }

  beforeEach(() => {
    render(<CorrectionView correction={correction} />)
  })

  it('Renders message', () => {
    expect(screen.getByText(correction.message)).toBeInTheDocument()
  })

  it('Renders suggestions', () => {
    expect(
      screen.getByText(correction.suggestions[0].value)
    ).toBeInTheDocument()
    expect(
      screen.getByText(correction.suggestions[1].value)
    ).toBeInTheDocument()
    expect(
      screen.getByText(correction.suggestions[1].short_description as string, {
        exact: false,
      })
    ).toBeInTheDocument()
  })
})
