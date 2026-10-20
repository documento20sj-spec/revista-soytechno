import Foundation
import Vision
import AppKit
for path in CommandLine.arguments.dropFirst() {
    guard let img = NSImage(contentsOfFile: path), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { print("\(path): sin imagen"); continue }
    let req = VNDetectBarcodesRequest()
    req.symbologies = [.qr]
    let h = VNImageRequestHandler(cgImage: cg, options: [:])
    try? h.perform([req])
    let vals = (req.results ?? []).compactMap { $0.payloadStringValue }
    print("\((path as NSString).lastPathComponent): \(vals.isEmpty ? "(no leído)" : vals.joined(separator: " | "))")
}
