$otBooks = @(
 @{n="Genesis";c=50},@{n="Exodus";c=40},@{n="Leviticus";c=27},@{n="Numbers";c=36},@{n="Deuteronomy";c=34},
 @{n="Joshua";c=24},@{n="Judges";c=21},@{n="Ruth";c=4},@{n="1 Samuel";c=31},@{n="2 Samuel";c=24},
 @{n="1 Kings";c=22},@{n="2 Kings";c=25},@{n="1 Chronicles";c=29},@{n="2 Chronicles";c=36},@{n="Ezra";c=10},
 @{n="Nehemiah";c=13},@{n="Esther";c=10},@{n="Job";c=42},@{n="Ecclesiastes";c=12},@{n="Song of Solomon";c=8},
 @{n="Isaiah";c=66},@{n="Jeremiah";c=52},@{n="Lamentations";c=5},@{n="Ezekiel";c=48},@{n="Daniel";c=12},
 @{n="Hosea";c=14},@{n="Joel";c=3},@{n="Amos";c=9},@{n="Obadiah";c=1},@{n="Jonah";c=4},@{n="Micah";c=7},
 @{n="Nahum";c=3},@{n="Habakkuk";c=3},@{n="Zephaniah";c=3},@{n="Haggai";c=2},@{n="Zechariah";c=14},@{n="Malachi";c=4}
)
$ntBooks = @(
 @{n="Matthew";c=28},@{n="Mark";c=16},@{n="Luke";c=24},@{n="John";c=21},@{n="Acts";c=28},
 @{n="Romans";c=16},@{n="1 Corinthians";c=16},@{n="2 Corinthians";c=13},@{n="Galatians";c=6},@{n="Ephesians";c=6},
 @{n="Philippians";c=4},@{n="Colossians";c=4},@{n="1 Thessalonians";c=5},@{n="2 Thessalonians";c=3},
 @{n="1 Timothy";c=6},@{n="2 Timothy";c=4},@{n="Titus";c=3},@{n="Philemon";c=1},@{n="Hebrews";c=13},
 @{n="James";c=5},@{n="1 Peter";c=5},@{n="2 Peter";c=3},@{n="1 John";c=5},@{n="2 John";c=1},@{n="3 John";c=1},
 @{n="Jude";c=1},@{n="Revelation";c=22}
)
$wisdomBooks = @(@{n="Psalms";c=150},@{n="Proverbs";c=31})

function Expand-Chapters($books) {
  $list = @()
  foreach ($b in $books) { for ($i=1; $i -le $b.c; $i++) { $list += , [PSCustomObject]@{book=$b.n; ch=$i} } }
  return $list
}

function Distribute-ToDays($list, [int]$days) {
  $buckets = New-Object 'System.Collections.Generic.List[object][]' $days
  for ($d=0; $d -lt $days; $d++) { $buckets[$d] = @() }
  $n = $list.Count
  for ($i=0; $i -lt $n; $i++) {
    $dayIndex = [math]::Floor($i * $days / $n)
    if ($dayIndex -ge $days) { $dayIndex = $days - 1 }
    $buckets[$dayIndex] += $list[$i]
  }
  return $buckets
}

function Format-Reading($items) {
  if ($items.Count -eq 0) { return "" }
  $groups = @()
  $curBook = $items[0].book
  $curStart = $items[0].ch
  $curEnd = $items[0].ch
  for ($i=1; $i -lt $items.Count; $i++) {
    $it = $items[$i]
    if ($it.book -eq $curBook -and $it.ch -eq ($curEnd + 1)) {
      $curEnd = $it.ch
    } else {
      $groups += , @{book=$curBook; s=$curStart; e=$curEnd}
      $curBook = $it.book; $curStart = $it.ch; $curEnd = $it.ch
    }
  }
  $groups += , @{book=$curBook; s=$curStart; e=$curEnd}
  $parts = $groups | ForEach-Object {
    if ($_.s -eq $_.e) { "$($_.book) $($_.s)" } else { "$($_.book) $($_.s)-$($_.e)" }
  }
  return ($parts -join "; ")
}

$days = 365
$otList = Expand-Chapters $otBooks
$ntList = Expand-Chapters $ntBooks
$wisdomList = Expand-Chapters $wisdomBooks

$otBuckets = Distribute-ToDays $otList $days
$ntBuckets = Distribute-ToDays $ntList $days
$wisdomBuckets = Distribute-ToDays $wisdomList $days

$rows = @()
for ($d=0; $d -lt $days; $d++) {
  $rows += [PSCustomObject]@{
    Day = $d + 1
    OldTestament = Format-Reading $otBuckets[$d]
    NewTestament = Format-Reading $ntBuckets[$d]
    Wisdom = Format-Reading $wisdomBuckets[$d]
  }
}

$rows | Export-Csv -Path "C:\Users\julia\Desktop\4-13\product\reading-plan.csv" -NoTypeInformation -Encoding UTF8
"Generated $($rows.Count) days"
$rows | Select-Object -First 5 | Format-Table -AutoSize
