<?PHP
   namespace Chirp;

  /*****************************************************************************
  * Chirp Internet                         www.chirp.com.au                    *
  * Created 2017-01-26                     Last Modified 2018-12-05            *
  * Duncan Crombie                         Duncan Crombie                      *
  ******************************************************************************
  * COPYRIGHT NOTICE                                                           *
  * (c) Copyright 2018-     Chirp Internet SRL. All Rights Reserved.           *
  *                                                                            *
  * Selling or modifying the code for this program without prior written       *
  * consent is expressly forbidden.  In other words, please ask first before   *
  * you try and make money off of this program.                                *
  *                                                                            *
  * Obtain permission before redistributing this software over the Internet or *
  * in any other medium.  In all cases copyright and header must remain intact.*
  *****************************************************************************/

  class Mazing
  {

    public $height;
    public $width;
    public $dist = -1;

    public $maze = [];

    public function __construct($height, $width)
    {
      $this->height = $height;
      $this->width = $width;

      $rows = $this->height * 2 + 1;
      $cols = $this->width * 2 + 1;

      // create border and entrance/exit
      for($i=0; $i < $rows; $i++) {
        for($j=0; $j < $cols; $j++) {
          if(($i == 0) || ($i == $rows - 1)) {
            $this->maze[$i][$j] = ['wall'];
          } else {
            if(($i % 2) == 1) {
              $this->maze[$i][$j] = (($j == 0) || ($j == $cols - 1)) ? ['wall'] : [];
            } else {
              $this->maze[$i][$j] = ($j % 2 == 0) ? ['wall'] : [];
            }
          }
        }
        if($i == 0) {
          $this->maze[$i][rand(1, $this->width) * 2 - 1] = ['door', 'exit'];
        }
        if($i == $rows - 1) {
          $this->maze[$i][rand(1, $this->width) * 2 - 1] = ['door', 'entrance'];
        }
      }

      // start partitioning
      $this->split(1, $this->height - 1, 1, $this->width - 1, TRUE);
    }

    private function pos_to_space($x)
    {
      return 2 * ($x-1) + 1;
    }

    private function pos_to_wall($x)
    {
      return 2 * $x;
    }

    private function split($r1, $r2, $c1, $c2, $doors=FALSE)
    {
      if($r2 < $r1) return;
      if($c2 < $c1) return;

      // create partition walls
      if($r1 == $r2) {
        $horiz = $r1;
      } else {
        $x = $r1+1;
        $y = $r2-1;
        $start = round($x + ($y-$x) / 4);
        $end = round($x + 3*($y-$x) / 4);
        $horiz = rand($start, $end);
      }
      if($c1 == $c2) {
        $vert = $c1;
      } else {
        $x = $c1+1;
        $y = $c2-1;
        $start = round($x + ($y-$x) / 3);
        $end = round($x + 2*($y-$x) / 3);
        $vert = rand($start, $end);
      }
      for($i=$this->pos_to_wall($r1)-1; $i <= $this->pos_to_wall($r2)+1; $i++) {
        for($j=$this->pos_to_wall($c1)-1; $j <= $this->pos_to_wall($c2)+1; $j++) {
          if(($i == $this->pos_to_wall($horiz)) || ($j == $this->pos_to_wall($vert))) {
            $this->maze[$i][$j] = ['wall'];
          }
        }
      }

      $gaps = [TRUE, TRUE, TRUE, FALSE];
      shuffle($gaps);

      // create gaps in partition walls
      if($gaps[0]) {
        $gap_at = rand($c1, $vert);
        $this->maze[$this->pos_to_wall($horiz)][$this->pos_to_space($gap_at)] = ($doors) ? ['door'] : [];
      }
      if($gaps[1]) {
        $gap_at = rand($vert+1, $c2+1);
        $this->maze[$this->pos_to_wall($horiz)][$this->pos_to_space($gap_at)] = ($doors) ? ['door'] : [];
      }
      if($gaps[2]) {
        $gap_at = rand($r1, $horiz);
        $this->maze[$this->pos_to_space($gap_at)][$this->pos_to_wall($vert)] = ($doors) ? ['door'] : []; 
      }
      if($gaps[3]) {
        $gap_at = rand($horiz+1, $r2+1);
        $this->maze[$this->pos_to_space($gap_at)][$this->pos_to_wall($vert)] = ($doors) ? ['door'] : [];
      }

      // split newly created chambers
      $this->split($r1, $horiz-1, $c1, $vert-1);
      $this->split($horiz+1, $r2, $c1, $vert-1);
      $this->split($r1, $horiz-1, $vert+1, $c2);
      $this->split($horiz+1, $r2, $vert+1, $c2);
    }

    public function is_wall(...$cells)
    {
      foreach($cells as $arr) {
        list($row, $col) = $arr;
        if(!$this->maze[$row][$col] || !in_array('wall', $this->maze[$row][$col])) {
          return FALSE;
        }
      }
      return TRUE;
    }

    public function is_gap(...$cells)
    {
      foreach($cells as $arr) {
        list($row, $col) = $arr;
        if(($row < 0) || ($col < 0)) {
          return FALSE;
        }
        if($this->maze[$row][$col]) {
          return FALSE;
        }
      }
      return TRUE;
    }

    public function is_nubbin(...$cells)
    {
      foreach($cells as $arr) {
        list($row, $col) = $arr;
        if(!$this->maze[$row][$col] || !in_array('nubbin', $this->maze[$row][$col])) {
          return FALSE;
        }
      }
      return TRUE;
    }

    public function remove_nubbins($percent = 100)
    {
      $rows = $this->height * 2 + 1;
      $cols = $this->width * 2 + 1;
      $percent = intval($percent);
      if(($percent < 1) || ($percent > 100)) {
        $percent = 100;
      }
      for($i=1; $i < $rows-1; $i++) {
        for($j=1; $j < $cols-1; $j++) {
          if(!$this->is_wall([$i, $j])) {
            continue;
          }
          if(rand(1, 100) > $percent) {
            continue;
          }
          if($this->is_wall([$i-1, $j-1], [$i-1, $j], [$i-1, $j+1], [$i+1, $j]) && $this->is_gap([$i+1, $j-1], [$i+1, $j+1], [$i+2, $j])) {
            $this->maze[$i][$j] = [];
            $this->maze[$i+1][$j] = ['nubbin'];
          }
          if($this->is_wall([$i-1, $j+1], [$i, $j-1], [$i, $j+1], [$i+1, $j+1]) && $this->is_gap([$i-1, $j-1], [$i, $j-2], [$i+1, $j-1])) {
            $this->maze[$i][$j] = [];
            $this->maze[$i][$j-1] = ['nubbin'];
          }
          if($this->is_wall([$i-1, $j-1], [$i, $j-1], [$i+1, $j-1], [$i, $j+1]) && $this->is_gap([$i-1, $j+1], [$i, $j+2], [$i+1, $j+1])) {
            $this->maze[$i][$j] = [];
            $this->maze[$i][$j+1] = ['nubbin'];
          }
          if($this->is_wall([$i-1, $j], [$i+1, $j-1], [$i+1, $j], [$i+1, $j+1]) && $this->is_gap([$i-1, $j-1], [$i-2, $j], [$i-1, $j+1])) {
            $this->maze[$i][$j] = [];
            $this->maze[$i-1][$j] = ['nubbin'];
          }
        }
      }
    }

    public function join_nubbins()
    {
      $rows = $this->height * 2 + 1;
      $cols = $this->width * 2 + 1;
      for($i=2; $i < $rows-2; $i += 2) {
        for($j=2; $j < $cols-2; $j += 2) {
          if(!$this->is_nubbin([$i, $j])) {
            continue;
          }
          if($this->is_nubbin([$i-2, $j])) {
            $this->maze[$i-2][$j][] = 'wall';
            $this->maze[$i-1][$j] = ['nubbin','wall'];
            $this->maze[$i][$j][] = 'wall';
          }
          if($this->is_nubbin([$i, $j-2])) {
            $this->maze[$i][$j-2][] = 'wall';
            $this->maze[$i][$j-1] = ['nubbin','wall'];
            $this->maze[$i][$j][] = 'wall';
          }
        }
      }
    }

    private function count_steps(&$arr, $r, $c, $val, $stop)
    {
      if(isset($arr[$r][$c]) && ($arr[$r][$c] <= $val)) {
        return;
      }
      if(!isset($this->maze[$r][$c])) {
        return;
      }
      if(!$this->is_gap([$r, $c]) && !in_array('door', $this->maze[$r][$c])) {
        return;
      }
      $arr[$r][$c] = $val;
      if($val && in_array($stop, $this->maze[$r][$c])) {
        return;
      }
      $this->count_steps($arr, $r-1, $c, $val+1, $stop);
      $this->count_steps($arr, $r, $c+1, $val+1, $stop);
      $this->count_steps($arr, $r+1, $c, $val+1, $stop);
      $this->count_steps($arr, $r, $c-1, $val+1, $stop);
    }

    public function place_keys()
    {
      $from_entrance = $from_exit = $furthest = [];
      $rows = $this->height * 2 + 1;
      $cols = $this->width * 2 + 1;
      for($j=1; $j < $cols-1; $j++) {
        if(in_array('entrance', $this->maze[$rows-1][$j])) {
          $this->count_steps($from_entrance, $rows-1, $j, 0, 'exit');
          break;
        }
      }
      for($j=1; $j < $cols-1; $j++) {
        if(in_array('exit', $this->maze[0][$j])) {
          $this->count_steps($from_exit, 0, $j, 0, 'entrance');
          break;
        }
      }
      $fc = $fr = -1;
      foreach($from_entrance as $r => $cols) {
        foreach(array_keys($cols) as $c) {
          if(isset($from_entrance[$r][$c], $from_exit[$r][$c])) {
            $furthest[$r][$c] = $from_entrance[$r][$c] + $from_exit[$r][$c];
            if($furthest[$r][$c] > $this->dist) {
              $fr = $r;
              $fc = $c;
              $this->dist = $furthest[$r][$c];
            }
          }
        }
      }
      if($this->is_nubbin([$fr-1,$fc-1]) && !$this->is_wall([$fr-1,$fc-1])) {
        $this->maze[$fr-1][$fc-1] = ['key'];
      } elseif($this->is_nubbin([$fr-1,$fc+1]) && !$this->is_wall([$fr-1,$fc+1])) {
        $this->maze[$fr-1][$fc+1] = ['key'];
      } elseif($this->is_nubbin([$fr+1,$fc-1]) && !$this->is_wall([$fr+1,$fc-1])) {
        $this->maze[$fr+1][$fc-1] = ['key'];
      } elseif($this->is_nubbin([$fr+1,$fc+1]) && !$this->is_wall([$fr+1,$fc+1])) {
        $this->maze[$fr+1][$fc+1] = ['key'];
      } else {
        $this->maze[$fr][$fc][] = 'key';
      }
    }

    public function place_sentinels($percent = 100)
    {
      $rows = $this->height * 2 + 1;
      $cols = $this->width * 2 + 1;
      $percent = intval($percent);
      if(($percent < 1) || ($percent > 100)) {
        $percent = 100;
      }
      for($i=1; $i < $rows-1; $i++) {
        for($j=1; $j < $cols-1; $j++) {
          if(!$this->is_wall([$i,$j])) {
            continue;
          }
          if(rand(1, 100) > $percent) {
            continue;
          }
          if($this->is_wall([$i-1,$j-1],[$i-1,$j],[$i-1,$j+1],[$i+1,$j-1],[$i+1,$j],[$i+1,$j+1])) {
            $this->maze[$i][$j][] = 'sentinel';
          }
          if($this->is_wall([$i-1,$j-1],[$i,$j-1],[$i+1,$j-1],[$i-1,$j+1],[$i,$j+1],[$i+1,$j+1])) {
            $this->maze[$i][$j][] = 'sentinel';
          }
        }
      }
    }

    public function display()
    {
      echo "<div id=\"maze\" data-steps=\"{$this->dist}\">\n";
      foreach($this->maze as $row) {
        echo "<div>";
        foreach($row as $cell) {
          echo "<div";
          if($cell) {
            echo " class=\"",implode(" ", $cell) . "\"";
          }
          echo "></div>";
        }
        echo "</div>\n";
      }
      echo "</div>\n";
    }

  }
?>
