import React, { useState } from 'react'
import { Correction, CorrectionLine } from '../interfaces/interfaces'
import CorrectionHighlighter from './CorrectionHighlighter'
import CorrectionView from './CorrectionView'

export default function Corrections({ text, corrections }: CorrectionLine) {
  const [selectedCorrection, setSelectedCorrection] = useState<Correction>(
    corrections[0]
  )
  return (
    <div data-testid="corrections">
      <CorrectionHighlighter
        text={text}
        corrections={corrections}
        selectedCorrection={selectedCorrection}
        setSelectedCorrection={setSelectedCorrection}
      />
      <CorrectionView correction={selectedCorrection} />
    </div>
  )
}
